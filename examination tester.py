# Student Exam Qualification and Passing Calculator

def calculate_required_exam_mark(current_average, exam_weight=0.6):
    """
    Calculate the minimum exam mark needed to pass the module (50% overall)
    
    Parameters:
    current_average: Student's current average (excluding exam)
    exam_weight: Weight of exam in final grade (default 60% = 0.6)
    
    Returns:
    Required exam mark to pass the module
    """
    # Formula: Final Mark = (Current Average * (1-exam_weight)) + (Exam Mark * exam_weight)
    # To pass: Final Mark >= 50
    # Therefore: Required Exam Mark = (50 - (Current Average * (1-exam_weight))) / exam_weight
    
    coursework_weight = 1 - exam_weight
    required_exam_mark = (50 - (current_average * coursework_weight)) / exam_weight
    
    return round(required_exam_mark, 1)

def check_qualification(average_mark):
    """
    Check if student qualifies to write the exam
    Minimum requirement: 40% average
    """
    MINIMUM_QUALIFYING_MARK = 40
    return average_mark >= MINIMUM_QUALIFYING_MARK

def get_passing_strategy(current_average):
    """
    Provide passing strategy based on current average
    """
    required_exam_mark = calculate_required_exam_mark(current_average)
    
    if required_exam_mark <= 0:
        return "You've already passed! No need to write the exam (but you still need to write it)"
    elif required_exam_mark <= 40:
        return f"You need to score {required_exam_mark}% in exam. This should be very achievable!"
    elif required_exam_mark <= 50:
        return f"You need to score {required_exam_mark}% in exam. Study smart and you'll get there!"
    elif required_exam_mark <= 60:
        return f"You need to score {required_exam_mark}% in exam. Put in consistent effort!"
    elif required_exam_mark <= 70:
        return f"You need to score {required_exam_mark}% in exam. This requires focused preparation!"
    elif required_exam_mark <= 80:
        return f"You need to score {required_exam_mark}% in exam. Challenge yourself and aim high!"
    elif required_exam_mark <= 90:
        return f"You need to score {required_exam_mark}% in exam. This will be tough but possible with dedication!"
    else:
        return f"You need to score {required_exam_mark}% in exam, which is currently impossible. Consider module revision options."

def main():
    print("=" * 60)
    print("STUDENT EXAM QUALIFICATION AND PASSING CALCULATOR")
    print("=" * 60)
    print("\nThis program will:")
    print("1. Check if you qualify to write the exam (minimum 40% average)")
    print("2. Calculate what exam mark you need to pass the module")
    print("\nAssumptions:")
    print("- Exam contributes 60% to final mark")
    print("- Coursework contributes 40% to final mark")
    print("- Passing mark is 50% overall")
    print("=" * 60)
    
    while True:
        try:
            # Get student's current average
            current_average = float(input("\nEnter your current average mark (%): "))
            
            if current_average < 0 or current_average > 100:
                print("Please enter a value between 0 and 100")
                continue
            
            print("\n" + "=" * 60)
            print("RESULTS")
            print("=" * 60)
            
            # Check qualification
            qualifies = check_qualification(current_average)
            
            if qualifies:
                print(f"\n✅ You QUALIFY to write the exam with {current_average}% average!")
                
                # Calculate required exam mark
                required_exam_mark = calculate_required_exam_mark(current_average)
                
                # Show the specific scenarios mentioned
                if current_average == 40:
                    print(f"\n📊 As per your scenario (40% average):")
                    print(f"You need to score {required_exam_mark}% in exam to pass the module")
                elif current_average == 60:
                    print(f"\n📊 As per your scenario (60% average):")
                    print(f"You need to score {required_exam_mark}% in exam to pass the module")
                
                # Show general result
                print(f"\n📝 To pass the module, you need to score: {required_exam_mark}% in the exam")
                
                # Provide strategy
                print(f"\n💡 Strategy: {get_passing_strategy(current_average)}")
                
                # Show calculation breakdown
                print(f"\n📐 Calculation breakdown:")
                print(f"Current coursework (40% weight): {current_average * 0.4:.1f} marks")
                print(f"Target final mark: 50%")
                print(f"Exam contribution needed: 50 - {current_average * 0.4:.1f} = {50 - (current_average * 0.4):.1f} marks")
                print(f"Required exam percentage: {required_exam_mark}% (of exam's 60% weight)")
                
            else:
                print(f"\n❌ You do NOT qualify to write the exam with {current_average}% average.")
                print(f"Minimum required: 40%")
                print(f"Shortfall: {40 - current_average:.1f}%")
                print("\n💡 Please speak to your lecturer about your options.")
            
            # Ask if user wants to check another student
            print("\n" + "=" * 60)
            again = input("\nWould you like to check another student? (yes/no): ").lower()
            if again != 'yes' and again != 'y':
                print("\nThank you for using the Student Exam Calculator. Good luck with your exams!")
                break
                
        except ValueError:
            print("Please enter a valid number")

def demonstrate_examples():
    """
    Demonstrate the program with example scenarios
    """
    print("\n" + "=" * 60)
    print("DEMONSTRATION EXAMPLES")
    print("=" * 60)
    
    # Test the specific scenarios mentioned
    test_cases = [40, 60, 35, 55, 75]
    
    for average in test_cases:
        print(f"\n{'='*40}")
        print(f"Student with {average}% average:")
        qualifies = check_qualification(average)
        
        if qualifies:
            required = calculate_required_exam_mark(average)
            print(f"✅ Qualifies for exam")
            print(f"📝 Needs {required}% in exam to pass")
            
            # Show the relationship
            if average == 40:
                print(f"✓ At 40% average → Need 60% in exam")
            elif average == 60:
                print(f"✓ At 60% average → Need 40% in exam")
        else:
            print(f"❌ Does NOT qualify for exam (needs 40% minimum)")

if __name__ == "__main__":
    # Run the demonstration first
    demonstrate_examples()
    
    # Then run the main interactive program
    main()
