import sys
import importlib
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Usage: uv run main.py <day> [example|input]")
        print("Example: uv run main.py 1 example")
        print("         uv run main.py 1 input")
        return

    day = sys.argv[1].zfill(2)  # Pad with zero if needed
    input_type = sys.argv[2] if len(sys.argv) > 2 else "input"

    try:
        # Import the day's module
        day_module = importlib.import_module(f"days.day{day}.solution")

        # Read the input file
        input_file = f"days/day{day}/{input_type}.txt"
        input_path = Path(input_file)

        if not input_path.exists():
            print(f"Input file {input_file} not found!")
            return

        with open(input_path) as f:
            data = f.read().strip()

        # Run both parts
        print(f"Day {day} - {input_type.capitalize()}")
        print("=" * 30)

        if hasattr(day_module, 'part1'):
            result1 = day_module.part1(data)
            print(f"Part 1: {result1}")

        if hasattr(day_module, 'part2'):
            result2 = day_module.part2(data)
            print(f"Part 2: {result2}")

    except ImportError:
        print(f"Day {day} solution not found! Create days/day{day}/solution.py")
    except FileNotFoundError:
        print(f"Input file for day {day} not found!")
    except Exception as e:
        print(f"Error running day {day}: {e}")

if __name__ == "__main__":
    main()
