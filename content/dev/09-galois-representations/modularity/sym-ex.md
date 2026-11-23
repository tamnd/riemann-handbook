---
id: sym-ex
title: A family of symbols in the tower with the six laws
kind: theorem
decl: UpperTheory.V.Z.Kato.Sym.symEx
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.KatoQuadraticCharacters.SymmetricPowerSymbols.SymEx
covers: 324
status: drafted
drafted_by: writer@claude
---
This theorem gives, for a tower $X$ and integers $\ell, c, d$, a family of unit-valued symbols with six laws. It is used by the lemma `ml` and by [the tame norm relation](/entry/kato-tame-relation-projected/), both below [the gluing of zeta classes](/entry/k4-top/). Its proof only passes eight proved lemmas to one assembly lemma.

## Statement

**Theorem.** Let $X$ be a tower over $(\Omega, \varepsilon)$, $\ell$ a prime, and $c, d > 1$ prime to 6. Then there is a family $w_n^M(s) \colon (\mathbb{Z}/M)^2 \times (\mathbb{Z}/M)^2 \to K^\times$ for $n, M \geq 0$ and $s \in \mathrm{Gal}(\Omega/\mathbb{Q})$ that satisfies `Laws`. For each $M > 0$ prime to $c$ and $d$, these laws say:

1. `coc`: $w_n^M$ is a cocycle modulo $\ell^n$-th powers and is locally constant;
2. `red`, `lev`, `dist`: compatibility in $n$, under a change of level, and under a sum over fibres, each up to a coboundary;
3. `isog`: a relation under $\mathrm{diag}(k, 1)$;
4. `top`: for $s$ that fixes $\mu_{M'}$, the image of $w_n^M(s)(x, y)$ under $\mathrm{diag}(k, 1)$ is the element `wGen` built from the Siegel functions `siegel X c x'` and `siegel X d y'`, up to a coboundary and an $\ell^n$-th power. We have not unfolded `wGen`.

## Proof

`symEx_of` takes `secEx`, `pSymb`, `pCoc`, `pRed`, `pLev`, `pDist`, `pIsog` and `pTop`. It picks the family from `pSymb`, and each other lemma gives one law. The real content is in those eight lemmas.

## In the Lean code

The theorem is one line in [SymEx.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/SymmetricPowerSymbols/SymEx.lean#L12). `SymEx` and `Laws` are in [WkTopEq.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/SymmetricPowerSymbols/WkTopEq.lean#L80), and `symEx_of` is in [SymExOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/SymmetricPowerSymbols/SymExOf.lean#L185). The statement does not ask that $c$ and $d$ be prime to $\ell$.
