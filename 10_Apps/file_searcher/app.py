import os
from collections import namedtuple

SearchResults = namedtuple('SearchResults',
                            'file, line, text')


def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print('Sorry we can\'t search that location.')
        return

    text = get_search_text_from_user()
    if not text:
        print('Sorry we can\'t search for nothing!')
        return

    matches = search_folders(folder, text)
    match_count = 0
    for m in matches:
        match_count += 1
        # print(m)
        print('------------- MATCH ---------------')
        print('file: ' + m.file)
        print('line: {}'.format(m.line))
        print('match: ' + m.text.strip())
        print()

    print('Found {:,} matches.'.format(match_count))


def print_header():
    print('-----------------------')
    print('      FILE SEARCH      ')
    print('-----------------------')
    print()


def get_folder_from_user():
    folder = input('What folder do you want to search? ')
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input('What are you searching for [single phrases only]? ')

    return text.lower()


def search_folders(folder, text):
    # all_matches = []
    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            matches = search_folders(full_item, text)
            # all_matches.extend(matches)

            # for m in matches:
            #     yield m       # generator

            yield from matches  # even better keyword as of python 3.3

        else:
            matches = search_file(full_item, text)
            # all_matches.extend(matches)

            # for m in matches:
            #     yield m

            yield from matches

    # return all_matches


def search_file(filename, search_text):
    # matches = []
    with open(filename, 'r', encoding='ISO-8859-1') as fin:

        line_num = 0
        for line in fin:
            line_num += 1
            if line.lower().find(search_text) >= 0:
                m = SearchResults(line=line_num, file=filename, text=line)
                # matches.append(m)
                yield m

        # return matches


if __name__ == "__main__":
    main()
