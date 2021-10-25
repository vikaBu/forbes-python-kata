from kata import data
from kata import forbes


def test_forbes_returns_correct_information():
    """Test original information returns correct results."""
    assert forbes() == ('oldest: ', 'Phil Knight', 24400000000, 'Nike',
                        'youngest: ', 'Mark Zuckerberg', 44600000000, 'Facebook')


def test_without_previous_two():
    """Test diffrent information returns correct results."""
    data.remove(data[5])
    data.remove(data[-17])
    assert forbes() == ('oldest: ', 'Carlos Slim Helu', 50000000000, 'telecom',
                        'youngest: ', 'Sergey Brin', 34400000000, 'Google')
