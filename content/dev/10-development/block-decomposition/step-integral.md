---
id: step-integral
title: The existence theorem on an integral closed subscheme
kind: theorem
decl: GlobalTheory.CompanionTheory.GE.step_integral
module: Development.AutomorphicSpectrum.Proofs.BlockDecomposition.GrothendieckExistenceClosed
covers: 366
status: drafted
drafted_by: writer@claude
---
This theorem is the main case of the Noetherian induction in [`statement_bot`](/entry/statement-bot/). It proves the statement $\mathrm{St}(\mathcal{J})$ of that entry when $V(\mathcal{J})$ is integral, given $\mathrm{St}(\mathcal{J}')$ for every larger ideal sheaf $\mathcal{J}'$. The plan is the one of EGA III$_1$, §5.1: reduce to the projective case by Chow's lemma, then use induction on the part where the Chow map is not an isomorphism.

## Statement

Let $A$, $I$ and $X$ be as in [`statement_bot`](/entry/statement-bot/), and let $\mathrm{St}(\mathcal{J})$ be the statement defined there.

**Theorem.** Let $\mathcal{J}$ be an ideal sheaf of $X$ such that $V(\mathcal{J})$ is integral. Suppose that $\mathrm{St}(\mathcal{J}')$ holds for each ideal sheaf $\mathcal{J}' \supsetneq \mathcal{J}$. Then $\mathrm{St}(\mathcal{J})$ holds.

## Proof

Let $E$ and $S_e$ satisfy the conditions of $\mathrm{St}(\mathcal{J})$. Put $V = V(\mathcal{J})$. It is separated, of finite type and quasi-compact over $A$.

1. **Chow cover.** `exists_chow_cover_integral` gives a closed subscheme $Y$ of $\mathbb{P}^N_A$, an open $O \subseteq Y$ and a proper map $\psi \colon O \to V$ over $A$. It is an isomorphism over a nonempty open $W \subseteq V$.
2. **The quasi-projective case.** `formal_existence_projective_open` gives $\mathrm{St}(0)$ on $O$.
3. **Pushforward.** `formal_existence_proper_pushforward` uses steps 1 and 2 to give a quasi-coherent $D \subseteq E$, an integer $c$ and an ideal sheaf $\mathcal{J}' \supsetneq \mathcal{J}$ such that $E/D$ has proper support, $S_{e+c} \subseteq D + I^{e+1}E$ for each $e$, and $\mathcal{J}' D \subseteq S_n$ for each $n$.
4. **Artin-Rees.** `artin_rees_closed_system` gives $c'$ such that the system $S'_e = (S_{e+c'} \cap D) + I^{e+1}D$ on $D$ satisfies the first and third conditions of $\mathrm{St}$. It also says: if $S'$ comes from a quotient of $D$ and $E/D$ has proper support, then $S$ comes from a quotient of $E$.
5. **Induction.** $D$ is coherent, by `coherent_subobject_coherent`. Step 3 and `restricted_system_killed_by_ideal` give $\mathcal{J}' D \subseteq S'_e$ for each $e$. So $\mathrm{St}(\mathcal{J}')$ applies to $D$ and $S'$. Step 4 then gives the result for $E$.

## In the Lean code

The theorem is at [GrothendieckExistenceClosed.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/GrothendieckExistenceClosed.lean#L22). The system $S'$ is `restrictSys I D S c'` in [PowSubSuccLe.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/PowSubSuccLe.lean#L45). Each named lemma is a second name, by a `first | exact ...` tactic, for a proof that we have not unfolded:

- `exists_chow_cover_integral` for `ChowOpen.exists_chow_open`;
- `formal_existence_projective_open` for `statement_open_projective`;
- `formal_existence_proper_pushforward` for `core_integral_step`;
- `artin_rees_closed_system` for `Comb.restrict_alg`;
- `coherent_subobject_coherent` for `isCoherent_subobject`;
- `restricted_system_killed_by_ideal` for `killed_restrictSys`.

So the real work of the step is in `core_integral_step` and `Comb.restrict_alg`. The open $W$ and the isomorphism over it go into `core_integral_step`. We have not unfolded how that proof uses them.
