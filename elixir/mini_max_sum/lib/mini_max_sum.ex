defmodule MiniMaxSum do
  @moduledoc """
  Documentation for MiniMaxSum.
  """

  @doc """
  main

  Input: Space separated list of integers as a string
    ex: "1 2 3 4 5"
  
  Output: Minimum and Maximum of sum of length - 1 elements from that list
    ex: "10 14"


  """
  def main(input) do
    input |> get_min_max_sum
  end

  def get_min_max_sum(input) do
    String.split(input, " ")
      |> Enum.map(fn x -> String.to_integer(x) end)
      |> Enum.reduce({10000, -10000, 0}, &ret_min_max_sum_tup(&1, &2))
      |> string_from_tuple
      # |> IO.puts
  end

  def ret_min_max_sum_tup(new, old) do
    {
      min(elem(old, 0), new),
      max(elem(old, 1), new),
      elem(old, 2) + new
    }
  end

  def string_from_tuple(input) do
    get_mini_sum_string(input) <> " " <> get_max_sum_string(input)
  end

  def get_mini_sum_string(input) do
    Integer.to_string(elem(input, 2) - elem(input, 1))
  end

  def get_max_sum_string(input) do
    Integer.to_string(elem(input, 2) - elem(input, 0))
  end

end
