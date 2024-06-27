import os

os.chdir("..")

def countlines(start, lines=0, header=True, begin_start=None):
    if header:
        print('{:>15} |{:>15} | {:<25}'.format('ADDED', 'TOTAL', 'FILE'))
        print('{:->11}|{:->11}|{:->20}'.format('', '', ''))

    for thing in os.listdir(start):
        thing = os.path.join(start, thing)
        if os.path.isfile(thing):
            with open(thing, 'r') as f:
                newlines = f.readlines()
                newlines = len(newlines)
                lines += newlines
            if begin_start is not None:
                reldir_of_thing = '.' + thing.replace(begin_start, '')
            else:
                reldir_of_thing = '.' + thing.replace(start, '')

            if os.path.splitext(reldir_of_thing)[1] in ['.png', '.jpeg', '.jpg']:
                continue

            print('{:>15} |{:>15} | {:<25}'.format(f"{newlines:,d}", f"{lines:,d}", reldir_of_thing))
        elif os.path.isdir(thing):
            lines = countlines(thing, lines, header=False, begin_start=start)
    return lines

# Example usage:
print(f"\n\nTotal lines : {countlines('Project'):,d}\n\n")



# Total lines : 18,577,532
# Coding lines : 
