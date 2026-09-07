        print("3. Peek Highest Priority Job")
        print("4. Display All Jobs")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            job_name = input("Enter Job Name: ")
            try:
                priority = int(input("Enter Priority (integer): "))
                scheduler.insert_job(job_name, priority)
            except ValueError:
                print("Invalid priority! Please enter an integer.")

        elif choice == "2":
            scheduler.delete_max_job()

        elif choice == "3":
            scheduler.peek_max_job()

        elif choice == "4":
            scheduler.display_heap()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice! Enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
