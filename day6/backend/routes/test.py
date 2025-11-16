from flask import jsonify
from flask_mail import Message

from mailing import mail
from .import bp_app

@bp_app.route('/send-test-email', methods=['GET'])
def send_test_email():
    msg = Message()
    msg.subject = "Test Email from Flask App"
    msg.recipients = ["recipient@example.com"]
    msg.body = "This is a test email sent from the Flask application to verify email functionality."
    msg.html = """<b>This is a test email sent from the Flask application to verify email functionality.</b>
    <a style="background-color:blue; color:white; padding:10px; border:none; border-radius:5px;" href="https://google.com">Click Me</a>"""
    mail.send(msg)
    return jsonify({"message": "Test email sent successfully!"})


@bp_app.route('/test_task', methods=['GET'])
def test_task():
    from backendjobs.tasks import find_person
    result = find_person.delay(1)
    while not result.ready():
        pass
    return jsonify({"task_id": result.id, "status": "Task has been queued.", "result": result.result.error if 'error' in result.result else result.result})