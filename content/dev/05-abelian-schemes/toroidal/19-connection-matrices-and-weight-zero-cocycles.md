---
title: Connection matrices and weight-zero cocycles
decls:
  - GlobalTheory.T.exists_weightZeroCocycle_eq_logDerivative_comb_add_coboundary
  - GlobalTheory.PullbackWeightZero.exists_comb_dlg_add_cob
  - GlobalTheory.PullbackWeightZero.h1_pull
  - GlobalTheory.T.exists_connection_matrix_invariant_basis
  - GlobalTheory.HeatInvLift.exists_invLift_symmKS
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Connection matrices and weight-zero cocycles

This section gives the two inputs of [the theorem on heat operators with polynomial defect](/entry/exists-basic-heat-poly-defect/) of Section 17 that are not about the periods. The first is a theorem on Čech $1$-cocycles of weight $0$ on the Raynaud extension $H$: each such cocycle is a combination of the logarithmic derivatives of the transition functions of $L$, plus a coboundary of weight $0$. The second is a theorem on lifts of a derivation $D$ of $R$ to $H$: on a suitable cover, the lifts can be chosen so that their differences are given by one symmetric matrix $\Theta$ over $R$. This matrix becomes the symbol of the heat operator. We use the notation of Section 17. In particular, $R$, $Q$, $O$, $H$ with $q : H \to A$, the basis $v_1, \dots, v_n$ and the invariant vector fields $\partial_1, \dots, \partial_n$ are fixed, and $\operatorname{dlg}_\delta(g_{\alpha\beta}) = \delta(q^* g_{\alpha\beta}) \cdot q^* g_{\alpha\beta}^{-1}$.

Let $Y$ be a scheme and $V_i$ for $i \in J$ opens of $Y$. A *Čech $1$-cochain* $z$ on the $V_i$ is a family of functions $z_{ii'}$ on $V_i \cap V_{i'}$. It is a *cocycle* if $z_{ii'} + z_{i'i''} = z_{ii''}$ on $V_i \cap V_{i'} \cap V_{i''}$ for all $i, i', i''$. It is a *coboundary* if there are functions $y_i$ on $V_i$ with $z_{ii'} = y_{i'} - y_i$ on $V_i \cap V_{i'}$. For opens $V_i$ of $A$ and a cochain $z$ on them, $q^* z$ is the cochain $(q^* z_{ii'})$ on the opens $q^{-1}(V_i)$.

In this section a *cover adapted to $L$* is a family of opens $V_i$ of $A$ for $i \in J$, with indices $\alpha(i)$, such that the $V_i$ cover $A$ and $V_i \subseteq A_{\alpha(i)}$ for each $i$. On $V_i \cap V_{i'}$ we write $g_{ii'} = g_{\alpha(i)\alpha(i')}$.

**Theorem 7.19.1 (Pulled back cocycles).** Let $R$, $Q$, $O$, $H$, $v$ and $\partial$ be as in Section 17, and let $(V_i, \alpha(i))$ be a cover adapted to $L$. Let $z$ be a Čech $1$-cocycle on the $V_i$. Then there are $c_1, \dots, c_n \in R$ and functions $y_i$ on $V_i$ such that on $q^{-1}(V_i) \cap q^{-1}(V_{i'})$
$$q^* z_{ii'} = \sum_b c_b\, \operatorname{dlg}_{\partial_b}(g_{ii'}) + (q^* y_{i'} - q^* y_i).$$

Lean: `GlobalTheory.PullbackWeightZero.h1_pull`.

*Proof.* There are three steps.

1. A lemma on the logarithmic derivative of the polarization along $q$ gives the following. There are tangent vectors $w_1, \dots, w_g$ of $A$ at the origin that span the tangent space, invariant vector fields $\partial'_1, \dots, \partial'_g$ on $A$ for them, an $n \times g$ matrix $M$ and a $g \times n$ matrix $N$ over $R$ with $NM = I_g$, such that
$$\operatorname{dlg}_{\partial_b}(g_{\alpha\beta}) = q^* \sum_a M_{ba}\, \partial'_a(g_{\alpha\beta})\, g_{\alpha\beta}^{-1}$$
on each open of $q^{-1}(A_\alpha \cap A_\beta)$, for each $b$.
2. A lemma on the Čech cohomology of $A$ applies to $w$, $\partial'$, the cover and $z$. It gives $c'_1, \dots, c'_g \in R$ and functions $y_i$ on $V_i$ such that
$$z_{ii'} = \sum_a c'_a\, \partial'_a(g_{ii'})\, g_{ii'}^{-1} + (y_{i'} - y_i)$$
on $V_i \cap V_{i'}$.
3. Put $c_b = \sum_a c'_a N_{ab}$. Pull back the identity of step 2 along $q$, and substitute the identity of step 1. Since $NM = I_g$,
$$\sum_b c_b \sum_{a'} M_{ba'} X_{a'} = \sum_{a'} \Bigl(\sum_a c'_a (NM)_{aa'}\Bigr) X_{a'} = \sum_a c'_a X_a$$
for each family $X_a$. With $X_a = q^*\bigl(\partial'_a(g_{ii'})\, g_{ii'}^{-1}\bigr)$ this gives the claim. $\square$

**Theorem 7.19.2 (Weight-zero cocycles).** Let $R$, $Q$, $O$, $H$, $v$ and $\partial$ be as in Section 17, and let $(V_i, \alpha(i))$ be a cover adapted to $L$. Let $z$ be a Čech $1$-cocycle on the opens $q^{-1}(V_i)$ of $H$ such that each $z_{ii'}$ has weight $0$. Then there are $c_1, \dots, c_n \in R$ and functions $y_i$ of weight $0$ on $q^{-1}(V_i)$ such that on $q^{-1}(V_i) \cap q^{-1}(V_{i'})$
$$z_{ii'} = \sum_b c_b\, \operatorname{dlg}_{\partial_b}(g_{ii'}) + (y_{i'} - y_i).$$

Lean: `GlobalTheory.PullbackWeightZero.exists_comb_dlg_add_cob` (also `GlobalTheory.T.exists_weightZeroCocycle_eq_logDerivative_comb_add_coboundary`, a second name).

*Proof.* There are four steps.

1. A lemma on the Raynaud extension says that a function of weight $0$ on $q^{-1}(V)$, for an open $V$ of $A$, is $q^* f'$ for exactly one function $f'$ on $V$. Conversely, $q^* f'$ has weight $0$ for each function $f'$ on $V$. Indeed, if $x$ and $x'$ are points of $H$ with $q(x) = q(x')$, then $(q^* f')(x') = f'(q(x')) = f'(q(x)) = (q^* f')(x)$, and the factor $c(0)$ is $1$.
2. By step 1, each $z_{ii'}$ is $q^* z'_{ii'}$ for a unique function $z'_{ii'}$ on $V_i \cap V_{i'}$. We show that $z'$ is a cocycle. Fix $i, i', i''$ and put $V = V_i \cap V_{i'} \cap V_{i''}$. The functions $z'_{ii'} + z'_{i'i''}$ and $z'_{ii''}$ on $V$ have the same pullback to $q^{-1}(V)$, since $z$ is a cocycle and pullback commutes with restriction. This pullback has weight $0$, so the uniqueness of step 1 gives $z'_{ii'} + z'_{i'i''} = z'_{ii''}$.
3. The theorem on pulled back cocycles applies to $z'$. It gives $c \in R^n$ and functions $y'_i$ on $V_i$ with $q^* z'_{ii'} = \sum_b c_b\, \operatorname{dlg}_{\partial_b}(g_{ii'}) + (q^* y'_{i'} - q^* y'_i)$.
4. Put $y_i = q^* y'_i$. By step 1, $y_i$ has weight $0$. Since $z_{ii'} = q^* z'_{ii'}$, step 3 gives the claim. $\square$

The next theorem chooses lifts of $D$ with differences in a fixed form. Its coefficient matrix is the *connection matrix* of the section title.

**Theorem 7.19.3 (Invariant lifts with a symmetric connection matrix).** Let $R$, $Q$, $O$, $H$, $v$ and $\partial$ be as in Section 17, and let $D$ be a derivation of $R$. Then there are a cover $(V_i, \alpha(i))$ adapted to $L$, a symmetric $n \times n$ matrix $\Theta$ over $R$, and lifts $d_i$ of $D$ on $q^{-1}(V_i)$, such that:

1. for each open $V'$ of $A$ with $q^{-1}(V') \subseteq q^{-1}(V_i)$ and each $\alpha \in X$, $d_i$ takes functions of weight $\alpha$ on $q^{-1}(V')$ to functions of weight $\alpha$;
2. on each open of $q^{-1}(V_i) \cap q^{-1}(V_{i'})$,
$$d_i - d_{i'} = \sum_{a,b} \Theta_{ab}\, \operatorname{dlg}_{\partial_b}(g_{ii'})\, \partial_a.$$

Lean: `GlobalTheory.HeatInvLift.exists_invLift_symmKS` (also `GlobalTheory.T.exists_connection_matrix_invariant_basis`, a second name).

*Proof.* There are five steps.

1. A lemma on lifts of derivations to the Raynaud extension gives a cover $(V_i, \alpha(i))$ adapted to $L$ and lifts $d^0_i$ of $D$ on $q^{-1}(V_i)$ that satisfy item 1.
2. A lemma on differences of such lifts gives Čech $1$-cocycles $z_1, \dots, z_n$ on the opens $q^{-1}(V_i)$, each with values of weight $0$, such that $d^0_i - d^0_{i'} = \sum_a z_{a,ii'}\, \partial_a$ on each open of $q^{-1}(V_i) \cap q^{-1}(V_{i'})$.
3. For each $a$, the theorem on weight-zero cocycles applies to $z_a$. It gives $c_{a1}, \dots, c_{an} \in R$ and functions $y_{a,i}$ of weight $0$ on $q^{-1}(V_i)$ with $z_{a,ii'} = \sum_b c_{ab}\, \operatorname{dlg}_{\partial_b}(g_{ii'}) + (y_{a,i'} - y_{a,i})$.
4. Put $d_i = d^0_i + \sum_a y_{a,i}\, \partial_a$. A lemma on invariant combinations says that $d_i$ is a lift of $D$ that satisfies item 1, because the $y_{a,i}$ have weight $0$ and the $\partial_a$ are invariant. On an open $W$ of $q^{-1}(V_i) \cap q^{-1}(V_{i'})$, steps 2 and 3 give
$$d_i - d_{i'} = \sum_a \bigl(z_{a,ii'} - (y_{a,i'} - y_{a,i})\bigr)\, \partial_a = \sum_{a,b} c_{ab}\, \operatorname{dlg}_{\partial_b}(g_{ii'})\, \partial_a.$$
Here we use that restriction commutes with $\partial_b$, with products and with pullback along $q$.
5. So the lifts $d_i$ satisfy item 2 with the matrix $C = (c_{ab})$, which need not be symmetric. A lemma on the Kodaira-Spencer relation for invariant lifts takes such a matrix $C$ and gives a symmetric matrix $\Theta$ for which item 2 holds with the same lifts $d_i$. $\square$

Only step 3 uses the theorem on weight-zero cocycles, and only through its statement for the cocycles $z_a$.

**Remark 7.19.4 (Formalization).** The proofs are in [ExistsWeightZeroCocycleEqLogDerivativeCombAddCob.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsWeightZeroCocycleEqLogDerivativeCombAddCob.lean#L60) and [ExistsConnectionMatrixInvariantBasis.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsConnectionMatrixInvariantBasis.lean#L68). The `T.*` names are wrappers, at line 16 of the matching `Statement` files, that close their goal with `first | exact @X | exact X | (intros; apply X <;> assumption)`. Cochains, cocycles and coboundaries are `C1`, `IsCoc` and `IsCob` in [IsInvDer.lean](lean:Development/AbelianVarietyTheory/Definitions/ModuliSpaces/IsInvDer.lean#L20) (lines 20, 22 and 25). The restriction `rsT` and the pullback `pbT` return $0$ when the target open is not contained in the source open, so the identities above are only meaningful on the opens where we state them. In the first file, `valR_pbT` (line 26) and `isWt_pbT` (line 33) prove the converse half of step 1 of the weight-zero theorem, and `descend` (line 41), `h1cover` (line 43) and `liepush` (line 45) restate `T.existsUnique_pullback_of_raynaudTorusWeight_zero`, `T.invariant_fields_cech_h1_relation` and `T.exists_logDeriv_polarization_raynaud_eq_pullback` as local theorems. The matrix identity of step 3 of the first proof is `alg_sum` (line 47). The cocycle property of step 2 of the weight-zero proof takes lines 86 to 101. The families $w$ and $\partial'$ on $A$ span the tangent space but are not asked to form a basis. In the second file, lines 26 to 60 are restriction lemmas, and the identity of step 4 is `hrel` (lines 81 to 101), closed by `ring` with `Matrix.of c`. The lemma `T.exists_symmetric_kodairaSpencer_invariantLifts` (line 102) takes any matrix $C$ with the relation and gives a symmetric $\Theta$; its statement does not say how $\Theta$ relates to $C$. The proofs also apply `T.exists_torusInvariant_derivationLifts_raynaudCover`, `T.difference_invariantLifts_isWeightZeroCechCocycle` and `T.torusInvariantLift_add_invariantCombination`. They have no entries in this chapter, and we use only their statements. We have not unfolded `Ray`, `IsWt` beyond Section 17, or the polarization lemma behind step 1 of the first proof.
