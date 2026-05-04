import unittest

def longest_consecutive_sequence(cards: list[int]) -> int:
    if not cards:
        return 0
        
    # Count the number of jokers
    jokers = cards.count(0)
    
    # Filter out zeros, remove duplicates, and sort
    unique_cards = sorted(list(set(c for c in cards if c != 0)))
    
    # If there are only jokers, the maximum length is the number of jokers
    if not unique_cards:
        return jokers
        
    max_len = 0
    left = 0
    
    # Move the right pointer through the unique cards
    for right in range(len(unique_cards)):
        # The number of holes (missing cards) between left and right
        holes = unique_cards[right] - unique_cards[left] - (right - left)
        
        # If there are more holes than jokers, shift the left pointer
        while holes > jokers:
            left += 1
            holes = unique_cards[right] - unique_cards[left] - (right - left)
            
        # Calculate current length: all cards in the window + all available jokers
        current_len = (right - left + 1) + jokers
        
        if current_len > max_len:
            max_len = current_len
            
    return max_len


# Writing tests using the unittest library
class TestPokerSequence(unittest.TestCase):

    def test_example_1(self):
        cards = [0, 10, 15, 50, 0, 14, 9, 12, 40]
        self.assertEqual(longest_consecutive_sequence(cards), 7)

    def test_example_2(self):
        cards = [1, 1, 1, 2, 1, 1, 3]
        self.assertEqual(longest_consecutive_sequence(cards), 3)

    def test_example_3(self):
        cards = [5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 0, 0]
        self.assertEqual(longest_consecutive_sequence(cards), 4)
        
    def test_all_jokers(self):
        cards = [0, 0, 0, 0]
        self.assertEqual(longest_consecutive_sequence(cards), 4)

    def test_empty_hand(self):
        cards = []
        self.assertEqual(longest_consecutive_sequence(cards), 0)

    def test_no_jokers_no_sequence(self):
        cards = [10, 20, 30]
        self.assertEqual(longest_consecutive_sequence(cards), 1)


if __name__ == '__main__':
    # Run the tests
    # argv=['first-arg-is-ignored'], exit=False allows safe execution in various environments
    unittest.main(argv=['first-arg-is-ignored'], exit=False)