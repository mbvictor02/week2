total_classes = int(input("Number of classes in the subject plan: ")) #Program asks user about 3 values that are stored as integers
exam_score = int(input("Exam Score (out of 100):  "))
attended_classes = int(input("Classes Attended (out of 40): "))

if (exam_score >= 70 and attended_classes/total_classes*100 >= 80):   #If else structure, condition to aprove:
    print("The student has passed")                                   #exam score plus or equal 70 and attended classes plus or equal 80%
else: 
    print("The student has failed")