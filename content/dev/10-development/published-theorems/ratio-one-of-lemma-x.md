---
id: ratio-one-of-lemma-x
title: The Euler ratio is one, from its coprime case
kind: theorem
decl: PositivityTheory.Lit1.GEN.ratioOne_of_lemmaX
module: Development.WeilBound.CoreStatements.PublishedTheorems.GlobalEulerCharacteristic.Assemble
covers: 827
status: drafted
drafted_by: writer@claude
---
This theorem proves Tate's global Euler characteristic formula in ratio form, for modules killed by a power of $\ell$, from the coprime case `GlobalEulerCharCoprime`. Its only use is [`globalEulerChar_of_lemmaX`](/entry/global-euler-char-of-lemma-x/), which translates the ratio into the formula of [`globalEulerChar_full`](/entry/global-euler-char-full/). This entry has the reductions of the proof. Below this theorem are 827 declarations.

## Statement

Let $\ell$ be a prime. Suppose that `GlobalEulerCharCoprime` holds.

**Theorem.** `RatioOne ℓ`. That is: let $K \subset \overline{\mathbb{Q}}$ be a number field, $S$ a finite set of finite places of $K$ that contains the places above $\ell$, and $G_{K,S}$ the Galois group of the maximal extension of $K$ unramified outside $S$. Let $M$ be a finite discrete $G_{K,S}$-module killed by $\ell^r$ for some $r$. Then `gsEulerRatio S M ιr` $= 1$, for each choice `ιr` of embeddings at the real places.

The ratio `gsEulerRatio` is $\chi(M) \cdot \#M^{r_1 + r_2} / \prod_{w \text{ real}} \#H^0(c_w, M)$, as in the parent entry.

## Proof

The proof is one line. It applies `ratioOne_of_killed_l` to the result of `W_assemble.ratioOneKilled_of_lemmaX`, applied to ℓ and `hX`. It has two parts.

**Modules killed by $\ell$.** `ratioOneKilled_of_lemmaX` proves `RatioOneKilled ℓ`, the case $\ell M = 0$.

1. `W_split.exists_split` finds a finite extension $L \supseteq K$, unramified outside $S$, such that the subgroup that fixes $L$ is normal and acts trivially on $M$. Also, $L$ contains a primitive $\ell$-th root of unity, and $\ell \neq 2$ or $L$ is totally complex. The field $L$ comes from the open kernel of the action.
2. `W_killed_c.ratio_eq_one_of_cyclic` makes $M$ a module over the finite group $\operatorname{Gal}(L/K)$ (`quot_rep`). The ratio is multiplicative in short exact sequences (`gs_multKilled`). By `eq_one_of_forall_isCyclic`, it is then enough to check modules coinduced from the subgroups $\operatorname{Gal}(L/K')$ with $\operatorname{Gal}(L/K')$ cyclic.
3. `W_killed_b.ratio_coind_cyclic` replaces a coinduced module by the restriction of $M$ to $K'$, with the places of $K'$ over $S$ (`exists_ratio_coind_eq_resTo`). It also reduces to the case where $[L:K']$ is prime to $\ell$ (`exists_prime_to_part`).
4. `W_endx.ending_lemmaX` checks the conditions of `GlobalEulerCharCoprime` for $K'$ and $L$, and applies `hX`.

**Dévissage.** `ratioOne_of_killed_l` goes from $\ell M = 0$ to $\ell^r M = 0$ by induction on $r$. For $r = 0$, $M = 0$ and the ratio is 1 (`gsEulerRatio_eq_one_of_subsingleton`). For the step, the sequence $0 \to M[\ell] \to M \to \ell M \to 0$ is exact (`rangeStepComplex_shortExact`). Here $M[\ell]$ is killed by $\ell$ and $\ell M$ by $\ell^r$, and the ratio is multiplicative (`ratio_shortExact_l`).

## In the Lean code

The theorem is in [Assemble.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/GlobalEulerCharacteristic/Assemble.lean#L13). `ratioOne_of_killed_l` in the same file is a second name for `W_devis.ratioOne_of_killed_l` in [WorkDevis.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/GlobalEulerCharacteristic/WorkDevis.lean#L9). `ratioOneKilled_of_lemmaX` is in [WorkAssemble.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/GlobalEulerCharacteristic/WorkAssemble.lean#L41). `RatioOne` and `RatioOneKilled` are in [RatioOneKilled.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/GlobalEulerCharacteristic/RatioOneKilled.lean#L7).

The same file has `ratioOneKilled_two`, a variant for $\ell = 2$ that ends with `W_endn.ending_narrow`. This proof does not use it. We have not opened `eq_one_of_forall_isCyclic`, `quot_rep` or `exists_prime_to_part`, so the descriptions of steps 2 and 3 come from their statements and names at the call sites.
