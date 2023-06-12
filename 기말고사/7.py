import paramiko
import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def create_ssh_connection():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    user = input('Username: ')
    pwd = getpass.getpass('Password: ')
    ssh.connect('114.71.220.5', 22, username=user, password=pwd)

    return ssh

def create_directory(ssh, dirname):
    cmd = f'mkdir {dirname}'
    ssh.exec_command(cmd)

def create_file(ssh, filename, content):
    cmd = f'echo {content} > {filename}'
    ssh.exec_command(cmd)

def create_zip_file(ssh, zip_filename, dirname):
    cmd = f'zip -r {zip_filename} {dirname}'
    ssh.exec_command(cmd)

def download_file(ssh, sftp, remote_filename, local_filename):
    sftp.get(remote_filename, local_filename)

def send_email(sender_email, sender_password, receiver_email, subject, attachment_path):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    with open(attachment_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {attachment_path}",
    )

    message.attach(part)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(message)

def main():
    user_id = input("본인 학번 입력: ")
    zip_filename = f"{user_id}.zip"
    directory_name = f"/home/net_pro/{user_id}"
    file_name = "iot.txt"
    file_content = "iot"

    ssh = create_ssh_connection()
    create_directory(ssh, directory_name)
    create_file(ssh, f"{directory_name}/{file_name}", file_content)
    create_zip_file(ssh, zip_filename, directory_name)

    sftp = ssh.open_sftp()
    download_file(ssh, sftp, zip_filename, zip_filename)
    sftp.close()
    ssh.close()

    sender_email = "gus12als@gmail.com"  # 발신자 이메일 주소
    sender_password = ""  # 발신자 이메일 암호
    receiver_email = "gus11als@naver.com"  # 수신자 이메일 주소
    subject = f"{user_id}.zip"  # 이메일 제목

    send_email(sender_email, sender_password, receiver_email, subject, zip_filename)

if __name__ == "__main__":
    main()
