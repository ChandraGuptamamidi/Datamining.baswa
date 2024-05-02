

        # Update analysis variables
        total_students += 1
        if placement_status == 'Placed':
            placed_students += 1
        avg_cgpa += cgpa

    # Calculate the average CGPA
    avg_cgpa /= total_students

    # Print the analysis results
    print (f"Total students: {total_students}")
    print (f"Number of placed students: {placed_students}")
    print (f"Number of not placed students: {total_students - placed_students}")
    print (f"Average CGPA: {avg_cgpa:.2f}")

# data pre processing
import csv

# Open the dataset file for reading
with open ('StudentID CGPA Internships Projects.txt', 'r') as file:
    # Create a CSV reader
    reader = csv.reader (file, delimiter='\t')

    # Read the header row
    header = next (reader)

    # Initialize lists to store the data
    student_ids = []
    cgpas = []
    internships = []
    projects = []
    workshops = []
    aptitude_scores = []
    soft_skills: list[float | Any] = []
    extracurricular = []
    placement_status = []
    ssc_marks = []
    hsc_marks = []

    # Iterate over each row in the dataset
    for row in reader:
        # Extract the data from each column in the row
        student_ids.append (int (row[0]))
        cgpas.append (float (row[1]))
        internships.append (int (row[2]))
        projects.append (int (row[3]))
        workshops.append (int (row[4]))
        aptitude_scores.append (int (row[5]))
        soft_skills.append (float (row[6]))
        extracurricular.append (row[7])
        placement_status.append (row[8])
        ssc_marks.append (int (row[9]))
        hsc_marks.append (int (row[10]))

# Handle missing data
mean_cgpa = sum (cgpas) / len (cgpas)
median_soft_skills = sorted (soft_skills)[len (soft_skills) // 2]

for i in range (len (cgpas)):
    if cgpas[i] == '':
        cgpas[i] = mean_cgpa
    if soft_skills[i] == '':
        soft_skills[i] = median_soft_skills

# Print the preprocessed dataset
print ("StudentID\tCGPA\tInternships\tProjects\tWorkshops/Certifications\tAptitudeTestScore\tSoftSkillsRating"
       "\tExtracurricularActivities\tPlacementStatus\tSSC_Marks\tHSC_Marks")
for i in range (len (student_ids)):
    print (
        f"{student_ids[i]}\t{cgpas[i]}\t{internships[i]}\t{projects[i]}\t{workshops[i]}\t{aptitude_scores[i]}\t{soft_skills[i]}\t{extracurricular[i]}\t{placement_status[i]}\t{ssc_marks[i]}\t{hsc_marks[i]}")
    # data splitting
    import csv
    from random import shuffle

    # Open the dataset file for reading
    with open ('StudentID CGPA Internships Projects.txt', 'r') as file:
        # Create a CSV reader
        reader = csv.reader (file, delimiter='\t')

        # Read the header row
        header = next (reader)

        # Initialize lists to store the data
        data = []
        for row in reader:
            data.append (row)

    # Shuffle the dataset randomly
    shuffle (data)

    # Calculate the split index
    split_index = int (0.8 * len (data))

    # Split the dataset into training set and test set
    training_data = data[:split_index]
    test_data = data[split_index:]

    # Save the training set to a new CSV file
    with open ('training_data.csv', 'w', newline='') as file:
        writer = csv.writer (file)
        writer.writerow (header)
        writer.writerows (training_data)

    # Save the test set to a new CSV file
    with open ('test_data.csv', 'w', newline='') as file:
        writer = csv.writer (file)
        writer.writerow (header)
        writer.writerows (test_data)

    print ("Dataset split into training set and test set successfully.")

import csv
import matplotlib.pyplot as plt

# Open the dataset file for reading
with open('StudentID CGPA Internships Projects.txt', 'r') as file:
    # Create a CSV reader
    reader = csv.reader(file, delimiter='\t')
      bn   +
    # Read the header row
    header = next(reader)

    # Initialize lists to store the data
    cgpas_placed = []
    cgpas_not_placed = []

    # Iterate over each row in the dataset
    for row in reader:
        # Extract the data from each column in the row
        cgpa = float(row[1])
        placement_status = row[11]

        # Append CGPA to the appropriate list based on placement status
        if placement_status == 'Placed':
            cgpas_placed.append(cgpa)
        else:
            cgpas_not_placed.append(cgpa)

# Plotting bar graphs for "Placed" and "Not Placed" students
plt.figure(figsize=(12, 6))

# Bar graph for "Placed" students
plt.subplot(1, 2, 1)
plt.hist(cgpas_placed, color='green', alpha=0.6)
plt.xlabel('CGPA')
plt.ylabel('Frequency')
plt.title('CGPA Distribution of Placed Students')

# Bar graph for "Not Placed" students
plt.subplot(1, 2, 2)
plt.hist(cgpas_not_placed, color='red', alpha=0.6)
plt.xlabel('CGPA')
plt.ylabel('Frequency')
plt.title('CGPA Distribution of Not Placed Students')

plt.tight_layout()
plt.show()
