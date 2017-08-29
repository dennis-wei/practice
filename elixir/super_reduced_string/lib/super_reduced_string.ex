defmodule SuperReducedString do
  @moduledoc """
  Documentation for SuperReducedString.
  """

  @doc """
  main

  reduces consectuive letters of strings

  """
  def main(input) do
    super_reduce([], input, false) |> IO.puts
  end

  def super_reduce(head, hd <> tail, change_made) do
    snd = hd(tail)
    cond do
      fst == snd -> super_reduce(head, remove_consecutive(tl(tail), fst), true)
      true -> super_reduce([head | fst], tail, change_made)
    end
  end

  def super_reduce(head, _, change_made) do
    cond do
      change_made -> super_reduce([], head, false)
      true -> head
    end
  end

  def remove_consecutive(hd <> tail, elem) do
    case hd do
      ^elem -> remove_consecutive(tail, elem)
      _ -> [hd | tail]
    end
  end

  def remove_consecutive(_, elem) do
    []
  end

end
