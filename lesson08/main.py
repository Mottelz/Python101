from Car import Car


def main():
    lucy = Car("Ford", "Mustang", 1967, 57133)
    lucy2 = Car("Ford", "Mustang", 1967, 57133)
    jack = Car("Honda", "Civic", 2022, 17)
    jack.log_trip(65)
    print(jack)
    print(lucy)

    print(lucy2 == lucy)


if __name__ == '__main__':
    main()
