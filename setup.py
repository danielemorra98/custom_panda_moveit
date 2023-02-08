from setuptools import setup
from glob import glob

package_name = 'custom_panda_moveit_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + "/launch", glob('launch/*.launch.py')),
        ('share/' + package_name + "/launch/config", glob('launch/config/*')),
        ('share/' + package_name + "/config", glob('config/*')),
        ('share/' + package_name + "/urdf", glob('urdf/*.urdf')),
        ('share/' + package_name + "/urdf/meshes/collision", glob('urdf/meshes/collision/*')),
        ('share/' + package_name + "/urdf/meshes/visual", glob('urdf/meshes/visual/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='daniele',
    maintainer_email='morradaniele@ymail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'launch_dummy_server = danielemorra_moveit_pkg.follow_joint_trajectory_server:main',
            'now_time_publisher = danielemorra_moveit_pkg.publisher_now_time:main',
            # '<name_exec> = <name_folder>.<name_file>:<name_function>',
        ],
    },
)
