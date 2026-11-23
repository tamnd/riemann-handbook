---
id: statement-bot
title: Algebraization of compatible quotients of a coherent sheaf
kind: theorem
decl: GlobalTheory.CompanionTheory.GE.statement_bot
module: Development.AutomorphicSpectrum.Proofs.BlockDecomposition.GrothendieckExistenceClosed
covers: 452
status: drafted
drafted_by: writer@claude
---
This theorem is the sheaf form of Grothendieck's existence theorem that [`geClosed`](/entry/ge-closed/) needs. It says that a compatible system of quotients of a coherent sheaf $E$ modulo powers of $I$, with proper support, comes from one quotient of $E$. The proof is a Noetherian induction on closed subschemes. Its hard case is [the integral step](/entry/step-integral/).

## Statement

Let $A$ be a Noetherian ring, complete for an ideal $I$. Let $X$ be separated, locally of finite type and quasi-compact over $A$. For a quasi-coherent ideal sheaf $\mathcal{J}$ on $X$, let $\mathrm{St}(\mathcal{J})$ be the following statement (`Statement I J`).

> Let $E$ be a coherent $\mathcal{O}_X$-module, and let $S_0, S_1, \dots$ be quasi-coherent subsheaves of $E$ such that
> 1. $I^{e+1}E \subseteq S_e$ and $S_e = S_{e+1} + I^{e+1}E$ for each $e$ (`ClosedSys`);
> 2. $\mathcal{J} E \subseteq S_e$ for each $e$, checked on affine opens (`Killed`);
> 3. the support of $E/S_0$ lies in a closed subscheme that is proper over $A$ (`PropSupp`).
>
> Then there is a quasi-coherent $B \subseteq E$ with $E/B$ supported in a closed subscheme proper over $A$ and $B + I^{e+1}E = S_e$ for each $e$ (`Alg`).

In words, $E/S_e$ is a compatible system of coherent quotients of $E/I^{e+1}E$, all living on $V(\mathcal{J})$, and $E/B$ is a quotient of $E$ that induces all of them.

**Theorem.** $\mathrm{St}(0)$ holds.

For $\mathcal{J} = 0$ condition 2 is empty, so $\mathrm{St}(0)$ is the statement with no condition on the support beyond 3.

## Proof

The scheme $X$ is Noetherian. By `ideal_sheaf_well_founded_gt`, the ideal sheaves of $X$ satisfy the ascending chain condition. So we may prove $\mathrm{St}(\mathcal{J})$ for each $\mathcal{J}$, assuming $\mathrm{St}(\mathcal{J}')$ for all $\mathcal{J}' \supsetneq \mathcal{J}$. There are three cases.

1. $\mathcal{J} = \mathcal{O}_X$. Then each $S_e = E$, and `formal_existence_top_ideal` gives the result.
2. $V(\mathcal{J})$ is integral. This is [`step_integral`](/entry/step-integral/).
3. Otherwise `noetherian_ideal_integral_or_split` gives $\mathcal{J}_1, \mathcal{J}_2 \supsetneq \mathcal{J}$ with $\mathcal{J}_1 \mathcal{J}_2 \subseteq \mathcal{J}$, so $V(\mathcal{J})$ is the union of two smaller closed subschemes. By induction $\mathrm{St}(\mathcal{J}_1)$ and $\mathrm{St}(\mathcal{J}_2)$ hold, and `formal_existence_product_ideal` gives $\mathrm{St}(\mathcal{J})$.

## In the Lean code

The theorem is at [GrothendieckExistenceClosed.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/GrothendieckExistenceClosed.lean#L47). `Statement`, `ClosedSys`, `Killed`, `PropSupp` and `Alg` are in [PowSubSuccLe.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/PowSubSuccLe.lean#L41). The subsheaf $I^n E$ is `powSub I E n`, the image of the sum of the generators of $I^n$ acting on $E$.

The lemmas it calls, each a second name for a proof in another file that we have not unfolded:

- `ideal_sheaf_well_founded_gt`;
- `formal_existence_top_ideal`;
- `noetherian_ideal_integral_or_split`;
- `formal_existence_product_ideal`;
- `step_integral`, in the same file.

The induction runs on the type `X.IdealSheafData` with the order $>$, through `WellFoundedGT.induction`.
