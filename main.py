import scripts.train_gan
import scripts.evaluate
import scripts.generate_fake_data
import scripts.file_deleter


def main():
    print("main")
    scripts.file_deleter.main()
    scripts.generate_fake_data.main()
    scripts.train_gan.main()
    scripts.evaluate.main()

if __name__ == "__main__":
    main()