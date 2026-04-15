How to use the Python scrips in the demos:
1. (Recommended) Create a Virtual Environment
Run the following command in any directory:
conda create --name myenv python=3.7

Run the following command to activate it:
conda activate myenv

2. Install Dependencies only within this environment.
First, navigate from the repository root to the OpenCatPythonAPI directory:
cd OpenCatPythonAPI

then execute the following command:
pip install -r requirements.txt

3. Run the Script
Navigate to the demos directory:
cd demos

then execute the following command to run a Python script (for example, petoiRobotExample.py):
python petoiRobotExample.py