import pytest
from math import pi
import sys
sys.path.append('../geometric_lib')
from calculate import calc


@pytest.mark.parametrize('side_length, expected_area, is_valid', [
    ({1}, 1, True),
    ({3}, 9, True),
    ({4}, 16, True),
    ({-2}, -4, False),
    ({0}, 0, True),
    ({5}, 25, True)
])
def test_square_area(side_length, expected_area, is_valid):
    result = calc('square', 'area', side_length)
    if is_valid:
        assert result == expected_area
    else:
        assert result != expected_area


@pytest.mark.parametrize('side_length, expected_perimeter, is_valid', [
    ({1}, 4, True),
    ({3}, 12, True),
    ({4}, 16, True),
    ({-3}, -12, False),
    ({0}, 0, True),
    ({2}, 8, True)
])
def test_square_perimeter(side_length, expected_perimeter, is_valid):
    result = calc('square', 'perimeter', side_length)
    if is_valid:
        assert result == expected_perimeter
    else:
        assert result != expected_perimeter
        

@pytest.mark.parametrize('sides, expected_area, is_valid', [
    ({3, 4, 5}, 6, True),
    ({5, 12, 13}, 30, True),
    ({8, 6, 10}, 24, True),
    ({-3, -4, 5}, -6, False),
])
def test_triangle_area(sides, expected_area, is_valid):
    result = calc('triangle', 'area', sides)
    if is_valid:
        assert abs(result - expected_area) < 1e-5
    else:
        assert result != expected_area


@pytest.mark.parametrize('sides, expected_perimeter, is_valid', [
    ({3, 4, 5}, 12, True),
    ({5, 12, 13}, 30, True),
    ({7, 24, 25}, 56, True),
    ({-5, -12, 13}, 26, False),
    ([3, 3, 3], 9, True)
])
def test_triangle_perimeter(sides, expected_perimeter, is_valid):
    result = calc('triangle', 'perimeter', sides)
    if is_valid:
        assert result == expected_perimeter
    else:
        assert result != expected_perimeter


@pytest.mark.parametrize('dimensions, expected_area, is_valid', [
    ({2, 3}, 6, True),
    ({-5, -4}, -20, False),
    ({6, 9}, 54, True),
    ({0, 5}, 0, True),
    ([10, 10], 100, True)
])
def test_rectangle_area(dimensions, expected_area, is_valid):
    result = calc('rectangle', 'area', dimensions)
    if is_valid:
        assert result == expected_area
    else:
        assert result != expected_area


@pytest.mark.parametrize('dimensions, expected_perimeter, is_valid', [
    ({4, 6}, 20, True),
    ({-4, -6}, 20, False),
    ([2, 2], 8, True),
    ({8, 15}, 46, True),
    ([60, 60], 240, True)
])
def test_rectangle_perimeter(dimensions, expected_perimeter, is_valid):
    result = calc('rectangle', 'perimeter', dimensions)
    if is_valid:
        assert result == expected_perimeter
    else:
        assert result != expected_perimeter


@pytest.mark.parametrize('radius, expected_area, is_valid', [
    ({1}, pi, True),
    ({2}, 4 * pi, True),
    ({-2}, -4 * pi, False),
    ({0}, 0, True),
    ({3}, 9 * pi, True)
])
def test_circle_area(radius, expected_area, is_valid):
    result = calc('circle', 'area', radius)
    if is_valid:
        assert abs(result - expected_area) < 1e-5
    else:
        assert result != expected_area


@pytest.mark.parametrize('radius, expected_perimeter, is_valid', [
    ({1}, 2 * pi, True),
    ({2}, 4 * pi, True),
    ({-2}, -4 * pi, False),
    ({0}, 0, True),
    ({5}, 10 * pi, True)
])
def test_circle_perimeter(radius, expected_perimeter, is_valid):
    result = calc('circle', 'perimeter', radius)
    if is_valid:
        assert abs(result - expected_perimeter) < 1e-5
    else:
        assert result != expected_perimeter
