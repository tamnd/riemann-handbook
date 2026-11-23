---
id: global-euler-char-of-lemma-x
title: The global Euler characteristic formula from its coprime case
kind: theorem
decl: PositivityTheory.Lit1.GEN.globalEulerChar_of_lemmaX
module: Development.WeilBound.CoreStatements.PublishedTheorems.GlobalEulerCharacteristic.GlobalEulerCharOfLemmaX
covers: 862
status: drafted
drafted_by: writer@claude
---
This theorem reduces Tate's global Euler characteristic formula to a special case, `GlobalEulerCharCoprime`. Its only use is [`globalEulerChar_full`](/entry/global-euler-char-full/), which applies it to `lemmaX` and states the formula in full. The proof is short. It calls [`ratioOne_of_lemmaX`](/entry/ratio-one-of-lemma-x/), which has most of the content, and then translates the result into the form of the statement. Below this theorem are 862 declarations.

## Statement

`GlobalEulerCharCoprime` is the coprime case that the parent entry describes, in ratio form. The field is a number field $K \subset \overline{\mathbb{Q}}$, $\ell M = 0$, and the action of the Galois group unramified outside $S$ factors through a Galois extension $L$ of degree prime to $\ell$, with $\mu_\ell \subset L$ and $\ell \neq 2$ or $L$ totally complex. The conclusion is that `gsEulerRatio` of $M$ is 1.

**Theorem.** If `GlobalEulerCharCoprime` holds, then `GlobalEulerChar` holds. That is, the formula of [`globalEulerChar_full`](/entry/global-euler-char-full/) holds for every number field $F$, prime $\ell$, finite $\mathbb{Z}/\ell^r$-module $M$ and set $S$.

## Proof

Fix $F$, $\Omega$, $\ell$, $r$, $M$, $S$ and the action `rhoS`. Then two steps follow.

1. `ratioOne_of_lemmaX ℓ hX` proves `RatioOne ℓ`. This is the formula in ratio form, for every number field $K \subset \overline{\mathbb{Q}}$ and every finite module killed by a power of $\ell$.
2. `globalEulerCharAt_of_ratioOne` turns `RatioOne ℓ` into the formula at $F$. It has three parts.
   - `dict_A` replaces the representation `rhoS` of $G_S$ over $\mathbb{Z}/\ell^r$ by a discrete `Rep` $A$ over $\mathbb{Z}$ of the Galois group unramified outside $S$. $A$ has the same order, the same orders of $H^0$, $H^1$ and $H^2$, and the same number of fixed points for each element.
   - `ratio_F` moves the ratio from subfields of $\overline{\mathbb{Q}}$ to $F$. An isomorphism $\Omega \cong \overline{\mathbb{Q}}$ sends $F$ to a subfield $K$ (`exists_fieldTransport`). The places, the Galois groups and the real places go along with it (`transport_data`). Two complex conjugations at the same real place are conjugate, so the order of the fixed points does not depend on the choice (`isCCAt_conj`).
   - The last part unfolds `eulerChar` and `archH0Card` and uses $r_1 + 2r_2 = [F:\mathbb{Q}]$ to clear the denominators.

## In the Lean code

The theorem is in [GlobalEulerCharOfLemmaX.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/GlobalEulerCharacteristic/GlobalEulerCharOfLemmaX.lean#L9). The proof is one line:

```
globalEulerCharAt_of_ratioOne S rhoS (ratioOne_of_lemmaX l hX)
```

`globalEulerCharAt_of_ratioOne` in [GlobalEulerCharAtOfRatioOne.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/GlobalEulerCharacteristic/GlobalEulerCharAtOfRatioOne.lean#L10) is a second name for the theorem of the same name in [WorkDictfwdA.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/GlobalEulerCharacteristic/WorkDictfwdA.lean#L315). `GlobalEulerCharCoprime` is in [LemmaX.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/GlobalEulerCharacteristic/LemmaX.lean#L8). `dict_A` only calls `W_dictfwd_b.dict_A`, which we have not opened.
