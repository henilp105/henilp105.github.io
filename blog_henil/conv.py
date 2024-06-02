def split_and_create_files(input_file, template_file):
    # Read content from the input file
    with open(input_file, 'r') as file:
        content = file.readlines()

    # Initialize variables
    result_dict = {}
    current_title = None
    current_content = []

    # Process each line in the content
    for line in content:
        if line.startswith("GSoC’22: Port fortran-lang.org to Sphinx || Blog post by Henil Shalin Panchal"):
            # If a new title is encountered, store the previous content
            if current_title is not None:
                result_dict[current_title] = ''.join(current_content)
                current_content = []

            # Set the new title
            current_title = line.strip()
        else:
            # Append the line to the current content
            current_content.append(line)

    # Add the last title and content
    if current_title is not None:
        result_dict[current_title] = ''.join(current_content)

    # Read the template file
    with open(template_file, 'r') as template:
        template_content = template.read()

    # Replace placeholders and create new files
    i=1
    for title, content in result_dict.items():
        new_content = template_content.replace('{title}', title).replace('{content}', content).replace('{slug}', title.strip().lower().replace(' ','-').replace('#',' '))

        # Write to a new file with the title as the filename
        output_file_name = f"GSoC 22: Port fortran-lang.org to Sphinx {i}.md"
        with open(output_file_name, 'w') as output_file:
            output_file.write(new_content.strip())

        print(f'File "{output_file_name}" created successfully.')
        i+=1
        # break

# Specify the file paths
input_file_path = 'content.md'
template_file_path = 'template.md'

# Call the function
split_and_create_files(input_file_path, template_file_path)
