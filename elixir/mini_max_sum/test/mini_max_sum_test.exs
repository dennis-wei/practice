defmodule MiniMaxSumTest do
  use ExUnit.Case
  doctest MiniMaxSum

  test "basic test" do
    assert MiniMaxSum.main("1 2 3 4 5") == "10 14"
  end

  test "negative numbers" do
    assert MiniMaxSum.main("-10 0 10") == ("-10 10")
  end

  test "unsorted numbers" do
    assert MiniMaxSum.main("3 5 1 2 4") == "10 14"
  end

end
