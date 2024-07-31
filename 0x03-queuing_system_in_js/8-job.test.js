const kue = require('kue');
const queue = kue.createQueue();
const chai = require('chai');
const expect = chai.expect;
const createPushNotificationsJobs = require('./8-job.js');

describe('createPushNotificationsJobs', () => {
  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');
  });

  it('should create jobs for each job in the jobs array', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
      { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account' },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
  });

  it('should log messages on job events', (done) => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
    ];

    const log = [];
    console.log = (message) => log.push(message);

    createPushNotificationsJobs(jobs, queue);

    queue.testMode.jobs[0].emit('complete');
    queue.testMode.jobs[0].emit('failed', 'Some error');
    queue.testMode.jobs[0].emit('progress', 50);

    expect(log).to.include(`Notification job created: ${queue.testMode.jobs[0].id}`);
    expect(log).to.include(`Notification job ${queue.testMode.jobs[0].id} completed`);
    expect(log).to.include(`Notification job ${queue.testMode.jobs[0].id} failed: Some error`);
    expect(log).to.include(`Notification job ${queue.testMode.jobs[0].id} 50% complete`);

    done();
  });
});
