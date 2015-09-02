def generate_lesson_HTML(lesson_title, lesson_body):
    html_text_1 = '''    
    <div class="lesson_title">
        ''' + lesson_title
    html_text_2 = '''
    </div>
        <div class="lesson_body">
        ''' + lesson_body
    html_text_3 = '''
        </div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def get_title(lesson):
    start_location = lesson.find('TITLE:')
    end_location = lesson.find('BODY:')
    lesson_title = lesson[start_location+7 : end_location-1]
    return lesson_title

def get_body(lesson):
    start_location = lesson.find('BODY:')
    lesson_body = lesson[start_location+6 :]
    return lesson_body

def get_lesson_by_number(text, lesson_number):
    counter = 0
    while counter < lesson_number:
        counter = counter + 1
        next_lesson_start = text.find('TITLE')
        next_lesson_end   = text.find('TITLE:', next_lesson_start + 1)
        if next_lesson_end >= 0:
            lesson = text[next_lesson_start:next_lesson_end]
        else:
            next_lesson_end = len(text)
            lesson = text[next_lesson_start:]
        text = text[next_lesson_end:]
    return lesson

TEST_TEXT = """TITLE: Structure and Repetition BODY: HTML is written in a tree-like structure, where elements have other elements inside of them. When using the developer tools, it is simple to see how the page is structured with boxes inside of boxes. Keeping this structure is very important for readability purposes and for understanding where certain elements will be on the page. While coding, it is important to not bog down the code with unnecessary repetition. For styling, instead of writing everything inline, it makes a lot more sense for a developer to use CSS to minimize repeated inline style code that would make the HTML more cumbersome and potentially lead to more errors. By using classes and referencing CSS, the developer knows she will get the same style every time. TITLE: How It All Works BODY: Your browser connects to the internet, which uses HTTP to communicate with servers. Servers are the same as your computer, except they are optimized for storing information. TITLE: HTML BODY: HTML stands for HyperText Markup Language. It is the language of the internet. Markup is what makes the webpage look a certain way. An HTML element contains an opening tag, content, and a closing tag. Computers are stupid because they can only interpret what a human writes for them. That's why we have to ensure that code is written properly. There are inline and block tags. Inline tags do not create line breaks. There are attributes, such as anchors and image sources. An img srouce attribute does not have an end tag and has no content. TITLE: The Relationship Between Computers and Programs BODY: A computer is a very powerful machine that cannot do anything without instructions. The speed at which a computer can process one cycle is close to light traveling 11 cm. Quite powerful, but not so smart - a computer needs a program, like peanut butter needs jelly. A program is a precise set of instructions that tells the computer what to do. Based on the program we write, we can basically get the computer to do almost anything we can imagine. Programs are written in languages. The language we are going to learn is Python. Computer languages, like speaking languages, have grammar and syntax that makes them work. Unlike speaking languages, they are unambiguous, which ensures that when the program is run, the computer will do exactly what the programmer wants it to do. 
"""

def generate_all_html(text):
    current_lesson_number = 1
    lesson = get_lesson_by_number(text, current_lesson_number)
    all_html = ''
    while lesson != '':
        title = get_title(lesson)
        body = get_body(lesson)
        lesson_html = generate_lesson_HTML(title, body)
        all_html = all_html + lesson_html
        current_lesson_number = current_lesson_number + 1
        lesson = get_lesson_by_number(text, current_lesson_number)
    return all_html

print generate_all_html(TEST_TEXT)
