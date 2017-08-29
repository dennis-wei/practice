defmodule Fibonacci do
  @moduledoc """
  Documentation for Fibonacci.
  """

  @doc """
  fib

  driver for fibonacci number calculator
  """

  def fib(n) do
    Enum.reduce(1..n, %{}, &put_in_map(&1, &2)) |> Map.get(n)
  end

  def put_in_map(elem, dp) do
    case elem do
      1 -> Map.put(dp, elem, 1)
      2 -> Map.put(dp, elem, 1)
      _ -> Map.put(dp, elem, Map.get(dp, elem - 1) + Map.get(dp, elem - 2))
    end
  end
end
