defmodule SuperReducedString do
  @moduledoc """
  Documentation for SuperReducedString.
  """

  @doc """
  main

  reduces consectuive letters of strings

  """
  def main(input) do
    input
      |> to_charlist
      |> super_reduce([], false)
      |> get_string
  end

  def get_string(input) do
    case input do
      [] -> "Empty String"
       _ -> input |> to_string
    end
  end

  def super_reduce([fst | tail], acc, change_made) do
    cond do
      tail != [] && fst == hd(tail) -> super_reduce(tl(tail), acc, true)
      true -> super_reduce(tail, acc ++ [fst], change_made)
    end
  end

  def super_reduce([], acc, change_made) do
    cond do
      change_made -> super_reduce(acc, [], false)
      true -> acc
    end
  end

end
