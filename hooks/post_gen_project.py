import os

package_dir = '{{cookiecutter.app_name}}'

package_name = '{{cookiecutter.package_name}}'

main = 'src/main/java/' + package_name.replace('.', '/')
test = 'src/test/java/' + package_name.replace('.', '/')

main_file_name = 'DemoApplication.java'
test_file_name = 'DemoApplicationTests.java'

os.makedirs(main, exist_ok=True)
os.makedirs(test, exist_ok=True)

os.rename(f'src/main/java/{main_file_name}', f'{main}/{main_file_name}')
os.rename(f'src/test/java/{test_file_name}', f'{test}/{test_file_name}')
