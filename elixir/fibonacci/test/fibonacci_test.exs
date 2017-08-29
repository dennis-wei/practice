defmodule FibonacciTest do
  use ExUnit.Case
  doctest Fibonacci

  test "base cases" do
    assert Fibonacci.fib(1) == 1
    assert Fibonacci.fib(2) == 1
  end

  test "10th number" do
    assert Fibonacci.fib(10) == 55
  end

  test "20th number" do
    assert Fibonacci.fib(20) == 6765
  end

  test "30th number" do
    assert Fibonacci.fib(30) == 832040
  end

  test "40th number" do
    assert Fibonacci.fib(40) == 102334155
  end

  test "50th number" do
    assert Fibonacci.fib(50) == 12586269025
  end
end
