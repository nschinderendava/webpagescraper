class WebPageScraper:

    def __init__(self, html):
        self.html = html
        self.tags_dict = {}

        if not self.validate():
            raise Exception('The provided HTML code is invalid.')

        self.body_content = self.get_body_content()
        self.excluded_tags = ['script', 'noscript']
        self.scrap()

    def scrap(self):
        i = 0
        n = len(self.body_content)
        while i < n:
            tag_initial_pos = self.body_content.find('<', i)
            if tag_initial_pos < 0:
                break

            next_char = self.body_content[tag_initial_pos + 1:tag_initial_pos + 2]
            if next_char == '/':
                i = self.body_content.find('>', tag_initial_pos) + 1
                continue

            is_comment = self.body_content[tag_initial_pos + 1:tag_initial_pos + 4] == '!--'
            if is_comment:
                i = tag_initial_pos + 1
                close_comment_tag_pos = self.body_content.find('-->', i) + 3
                next_open_comment_tag_pos = (self.body_content.find('<!--', i) + 4) if self.body_content.find('<!--',
                                                                                                    i) >= 0 else False
                while next_open_comment_tag_pos and next_open_comment_tag_pos < close_comment_tag_pos:
                    close_comment_tag_pos = self.body_content.find('-->', close_comment_tag_pos) + 3
                    next_open_comment_tag_pos = (
                                self.body_content.find('<!--', close_comment_tag_pos) + 4) if self.body_content.find('<!--',
                                                                                                           close_comment_tag_pos) >= 0 else False
                i = close_comment_tag_pos
                continue

            new_line_char = chr(10)
            open_tag_end_pos = self.body_content.find('>', tag_initial_pos)
            current_tag = self.body_content[tag_initial_pos + 1:open_tag_end_pos].split(' ')[0].replace('/', '').replace(
                new_line_char, '')

            i = open_tag_end_pos + 1

            if current_tag in self.excluded_tags:
                i = self.body_content.find('/' + current_tag + '>', i) + len('/' + current_tag + '>')
                continue

            if current_tag in self.tags_dict:
                self.tags_dict[current_tag] = self.tags_dict[current_tag] + 1
            else:
                self.tags_dict[current_tag] = 1

    def get_tags(self):
        return self.tags_dict

    def get_total_nb_of_elements(self):
        sum = 0
        for tag in self.tags_dict:
            sum = sum + self.tags_dict[tag]
        return sum

    def get_total_nb_of_html_tags(self):
        return len(self.tags_dict)

    def get_most_used_tags(self, limit = None):
        sorted_list = sorted(self.tags_dict.items(), key=lambda x: x[1], reverse=True)
        mosted_used_tags = {}
        counter = 0
        for (key,value) in sorted_list:
            mosted_used_tags[key] = str(value)
            counter += 1
            if counter == limit:
                break
        return mosted_used_tags

    def get_body_content(self):
        bodyOpenTagPosInitial = self.html.find('<body', 0)
        bodyOpenTagPosEnd = self.html.find('>', bodyOpenTagPosInitial)
        initialPos = bodyOpenTagPosEnd + 1
        endPos = self.html.find('/body>', initialPos) - 1
        return self.html[initialPos:endPos]

    def validate(self):
        counterInicio = 0
        counterFinal = 0
        for char in self.html:
            if char == '<':
                counterInicio = counterInicio + 1
            elif char == '>':
                counterFinal = counterFinal + 1
                if counterFinal > counterInicio:
                    return False
        return counterInicio == counterFinal

