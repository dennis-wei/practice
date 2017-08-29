defmodule SuperReducedStringTest do
  use ExUnit.Case
  doctest SuperReducedString

  test "basic test" do
    assert SuperReducedString.main("aab") == "b"
  end

  test "empty test" do
    assert SuperReducedString.main("aabb") == ""
  end
  
  test "reduce to empty test" do
    assert SuperReducedString.main("abba") == ""
  end

  test "multiple letters" do
    assert SuperReducedString.main("aaa") == ""
  end

end
