defmodule BirthdayCakeCandlesTest do
  use ExUnit.Case
  doctest BirthdayCakeCandles

  test "basic test" do
    assert BirthdayCakeCandles.main("4\n3 2 1 3") == 2
  end
end
