defmodule AppleOrangeTest do
  use ExUnit.Case
  doctest AppleOrange

  test "basic test" do
    assert AppleOrange.main("7 11\n5 15\n3 2\n-2 2 1\n5 -6") == "1\n1"
  end
end
