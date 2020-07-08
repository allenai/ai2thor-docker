from invoke import task
import boto3
import subprocess
import os
import glob
import tempfile
import platform


@task
def extract_store_nvidia_driver(context, cuda_url):
    if platform.system() != "Linux":
        raise Exception("CUDA driver extraction can only be run on Linu")

    name = os.path.basename(cuda_url)
    subprocess.run("wget -O '%s' '%s'" % (name, cuda_url), shell=True)
    os.chmod(name, 0o755)
    with tempfile.TemporaryDirectory() as tf_name:
        subprocess.check_call("./%s --extract=%s" % (name, tf_name), shell=True)
        drivers = list(glob.glob('%s/NVIDIA-Linux-x86_64-*.run' % tf_name))
        if drivers:
            driver_path = drivers[0]
            print("Storing driver %s at s3://ai2thor-vision-nvidia" % driver_path)
            with open(driver_path, "rb") as f:
                data = f.read()

            key = os.path.basename(driver_path)

            s3 = boto3.resource("s3")
            s3.Object('ai2-vision-nvidia', key).put(
                Body=data, ACL="public-read", ContentType="text/x-shellscript"
            )
        else:
            raise Exception("no drivers found in %s" % name)
    
    os.unlink(name)
