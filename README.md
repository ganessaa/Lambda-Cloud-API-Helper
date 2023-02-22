# Lambda Cloud API with Python

This is a sample of using the [Lambda Cloud API](https://cloud.lambdalabs.com/api/v1/docs) from Python. [API keys](https://cloud.lambdalabs.com/api-keys) and [SSH keys](https://cloud.lambdalabs.com/ssh-keys) must be set up in advance.

## Execution environment construction

### Get clone of this code

```bash
git clone --depth 1 https://github.com/ganessaa/lambda-cloud-api-python
cd ./lambda-cloud-api-python
```

### (option)Create a virtual environment

You can also build a virtual environment with [venv](https://docs.python.org/3/library/venv.html), etc.

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install requirements

```bash
pip install -r requirements.txt
```

### Environment Variable Settings

Create a `.env` file and set the API key you generated in [API keys](https://cloud.lambdalabs.com/api-keys) and the SSH key name you added in [SSH keys](https://cloud.lambdalabs.com/ssh-keys).

```bash
vi .env
# code .env
```

```.env
API_KEY=xxxxxxxx
SSH_KEY_NAME=xxxxxxxx
```

## Execute Lambda Cloud API

### Launch instances

Specify the instance type name and region to launch the instance.

```bash
python launch.py --instance_type_name gpu_1x_a10 --region_name us-west-1
# python launch.py --instance_type_name gpu_1x_a100_sxm4 --region_name us-east-1 
```

### Terminate an instance

Specify instance IDs and terminate the instance. Multiple IDs can be specified and terminated at once.

```bash
python terminate.py --ids xxxxxxxx xxxxxxxx
```

### List running instances

```bash
python instances.py
```

### List details of a specific instance

```bash
python instances.py --id xxxxxxxx
```

### Retrieve list of offered instance types

```bash
python instance_types.py
```
