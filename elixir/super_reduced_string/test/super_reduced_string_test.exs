defmodule SuperReducedStringTest do
  use ExUnit.Case
  doctest SuperReducedString

  test "basic test" do
    assert SuperReducedString.main("aab") == "b"
  end

  test "empty test" do
    assert SuperReducedString.main("aabb") == "Empty String"
  end

  test "only one reduction" do
    assert SuperReducedString.main("aa") == "Empty String"
  end
  
  test "reduce to empty test" do
    assert SuperReducedString.main("abba") == "Empty String"
  end

  test "multiple letters" do
    assert SuperReducedString.main("aaa") == "a"
  end

  test "test 1" do
    assert SuperReducedString.main("aaabccddd") == "abd"
  end

end
