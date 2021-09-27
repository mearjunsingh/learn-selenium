from selenium import webdriver
from programiz_python import config


class PythonCompiler(webdriver.Chrome):
    def __init__(self, driver_path=config.DRIVER_PATH, tear_down=False):
        self.tear_down = tear_down

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        if not config.OPEN_WINDOW:
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument('--window-size=1920,1080')
        
        super(PythonCompiler, self).__init__(executable_path=driver_path, options=options)
        self.maximize_window()
        self.implicitly_wait(15)
    

    def __exit__(self, *args) -> None:
        if self.tear_down:
            self.quit()
    

    def land_compiler(self):
        self.get('https://www.programiz.com/python-programming/online-compiler/')
    

    def input_code(self, code):
        editor_variable_name = '' 
        new_content = ''
        script = f"""
        var editor = ace.edit('editor');
        editor.setValue(`{code}`);
        """
        self.execute_script(script, editor_variable_name, new_content)
    

    def render_code(self):
        run_btn = self.find_element_by_xpath('//*[@id="root"]/div[3]/div[4]/div[1]/div[2]/button[3]')
        run_btn.click()


    def fetch_output(self):
        script = """
        return ace.edit('terminal').getValue();
        """
        result = self.execute_script(script)
        print(result)