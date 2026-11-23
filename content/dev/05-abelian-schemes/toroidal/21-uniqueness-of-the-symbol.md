---
title: Uniqueness of the symbol
decls:
  - GlobalTheory.HeatSym.vertical_symbol_zero
  - GlobalTheory.T.verticalSymbol_zero_of_bracket_preserving
  - GlobalTheory.HeatSym.symbol_unique
  - GlobalTheory.T.heatOperator_symbol_unique_principalPolarisation
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Uniqueness of the symbol

This section proves the uniqueness lemma of step 8 in the proof of [the theorem on the symbol of a commuting heat operator](/entry/is-ks-of-heat/) of Section 20. Two second-order operators of the form $\mathcal{H}_k$ that preserve the values of level $k$ at a formal point of $G$ have the same symbol. The proof has two steps. A bracket of the difference of the two operators removes the terms of order $0$ and $1$ in the vertical directions. The result is a first-order condition on the symbol alone. A lemma on the generic fibre, which is a polarized abelian variety over a field of characteristic $0$, then shows that the symbol is zero. We use the notation of Sections 17 and 20.

We fix the data of the main theorem of Section 20. So $R$ is a complete Noetherian local domain that contains $\mathbb{Q}$, $t$ is a semi-abelian datum on $\operatorname{Spec} R$ with group $G$ and line bundle $L$, and $P$ is a uniformization of $t$ by degeneration data $Q$. We suppose that $Q$ is monomial in nonzero $t_1, \dots, t_m$ with exponents $\gamma$, and that the abelian locus of $G$ is the basic open $D(t_1 \cdots t_m)$. Let $v'_1, \dots, v'_n$ be a basis of the tangent vectors of $G$ at the origin and $\partial'_1, \dots, \partial'_n$ invariant vector fields for them.

A *framed formal point* of $G$ consists of a local domain $\Omega$, a ring map $\varphi : R \to \Omega$, a point $x'$ of $G$ over $\operatorname{Spec} \Omega$, derivations $\delta_1, \dots, \delta_n$ of $\Omega$ and a generator $g$ of the pullback of $L$ along $x'$, such that:

1. $\Omega$ is complete for the $\varphi(\mathfrak{m}_R)\Omega$-adic topology, and $x'$ lies over $\operatorname{Spec} \varphi$;
2. $\delta_a(\varphi(r)) = 0$ for each $r \in R$ and each $a$;
3. $x'^*(\partial'_a f) = \delta_a(x'^* f)$ for each function $f$ on an open in which $x'$ lands;
4. if $f$ is such a function and $x'^* f = 0$, then $f = 0$.

These are the properties of steps 2 to 5 in the proof of Section 20. We extend each $\delta_a$ to a derivation of $\operatorname{Frac} \Omega$ and keep the name $\delta_a$. For $k \ge 1$ let $V_k \subseteq \operatorname{Frac} \Omega$ be the set of values of level $k$, as in step 5 of Section 20: $s \in V_k$ if $\varphi(r)\, s$ is the value of a section of $L^k$ at $x'$ in the trivialization $g^k$, for some nonzero $r \in R$.

The sets $V_k$ have three closure properties. Let $s \in V_j$ and $s' \in V_{j'}$, with $\varphi(r)\, s = x'^* \sigma$ and $\varphi(r')\, s' = x'^* \sigma'$. Since $x'$ lies over $\operatorname{Spec} \varphi$, the value of the constant function $r$ at $x'$ is $\varphi(r)$.

1. If $j = j'$, then $\varphi(r r')(s - s') = x'^*(r' \sigma - r \sigma')$. Since $R$ is a domain, $r r' \neq 0$, so $s - s' \in V_j$.
2. The product $\sigma \sigma'$ is a section of $L^{j + j'}$, and $\varphi(r r')\, s s' = x'^*(\sigma \sigma')$ in the trivialization $g^{j+j'}$. So $s s' \in V_{j + j'}$.
3. If $2 s \in V_j$, with $\varphi(r)(2 s) = x'^* \sigma$, then $\varphi(2 r)\, s = x'^* \sigma$. Since $R$ contains $\mathbb{Q}$, $2 r \neq 0$, so $s \in V_j$.

For a derivation $\delta$ of $\operatorname{Frac} \Omega$, a symmetric matrix $\Lambda$ over $\operatorname{Frac} \Omega$, $k \in \mathbb{N}$ and $b, c \in \operatorname{Frac} \Omega$, put
$$\beta_k(\delta, \Lambda; b, c) = k\, b\, (b\, \delta c - c\, \delta b) - \sum_{a, e} \Lambda_{ae}\, \delta_a b\, (b\, \delta_e c - c\, \delta_e b).$$
We call it the *bracket*. It contains only first derivatives, and it vanishes for $c = b$.

**Theorem 7.21.1 (Vanishing of a vertical symbol).** Let $(\Omega, \varphi, x', \delta, g)$ be a framed formal point of $G$. Let $\delta_0$ be a derivation of $\operatorname{Frac} \Omega$ with $\delta_0(\varphi(r)) = 0$ for each $r \in R$, and let $\Lambda$ be a symmetric $n \times n$ matrix over $\operatorname{Frac} \Omega$. Suppose that $\beta_k(\delta_0, \Lambda; b, c) \in V_{3k}$ for each $k \ge 1$ and all $b, c \in V_k$. Then $\Lambda = 0$.

Lean: `GlobalTheory.HeatSym.vertical_symbol_zero` (also `GlobalTheory.T.verticalSymbol_zero_of_bracket_preserving`, a second name).

*Proof.* Let $K = \operatorname{Frac} R$. There are seven steps.

1. A lemma on generic points gives a ring map $\psi : K \to \operatorname{Frac} \Omega$ that extends $\varphi$, and a point $\xi$ of the generic fibre $A_K$ of $G$ over $\operatorname{Spec} \psi$ such that $\xi^* f = 0$ implies $f = 0$. Here $A_K$ is an abelian variety over $K$ with the polarization that $L$ gives.
2. A lemma on the generic fibre gives a basis of the tangent vectors of $A_K$ at the origin and invariant vector fields $\partial^K_a$ for it, with $\xi^*(\partial^K_a f) = \delta_a(\xi^* f)$.
3. A dictionary lemma gives an open $U_0$ of the trivializing cover of the line bundle $L_K$ of $A_K$ in which $\xi$ lands, and a unit $q$ of $\operatorname{Frac} \Omega$, such that for each $k \ge 1$ an element $s$ lies in $V_k$ if and only if $s = q^k\, \xi^* \sigma$ for a section $\sigma$ of $L_K^k$, with the value taken in the trivialization on $U_0$.
4. A derivation $\delta'$ of $\operatorname{Frac} \Omega$ that kills $\varphi(R)$ kills $\psi(K)$. Indeed each element of $K$ is $a / b$ with $a, b \in R$, and $\delta'(\psi(a) / \psi(b)) = (\psi(b)\, \delta' \psi(a) - \psi(a)\, \delta' \psi(b)) / \psi(b)^2 = 0$. In particular this holds for $\delta_0$ and for each $\delta_a$.
5. Put $\delta_1 = \delta_0 - \sum_{a, e} \Lambda_{ae}\, (\delta_a q / q)\, \delta_e$. This is a derivation of $\operatorname{Frac} \Omega$, as a combination of derivations, and it kills $\psi(K)$ by step 4.
6. Let $b = q^k b'$ and $c = q^k c'$. For each derivation $\delta$ we have $b\, \delta c - c\, \delta b = q^{2k}(b'\, \delta c' - c'\, \delta b')$, and $\delta_a b = q^k(\delta_a b' + k\, (\delta_a q / q)\, b')$. If we insert this in $\beta_k$, the terms with $\delta_a q$ combine with the first term, and
$$\beta_k(\delta_0, \Lambda; b, c) = q^{3k}\, \beta_k(\delta_1, \Lambda; b', c').$$
7. Let $k \ge 1$ and let $\sigma, \tau$ be sections of $L_K^k$, with $b' = \xi^* \sigma$ and $c' = \xi^* \tau$. By step 3, $q^k b'$ and $q^k c'$ lie in $V_k$. By the hypothesis, $\beta_k(\delta_0, \Lambda; q^k b', q^k c') \in V_{3k}$. By step 3 again, this element is $q^{3k}\, \xi^* \rho$ for a section $\rho$ of $L_K^{3k}$. By step 6 and since $q$ is a unit, $\beta_k(\delta_1, \Lambda; \xi^* \sigma, \xi^* \tau) = \xi^* \rho$.

A lemma on polarized abelian varieties over a field of characteristic $0$ now applies. It takes $A_K$, the fields $\partial^K_a$, the point $\xi$, the open $U_0$, a derivation that kills $\psi(K)$ and a symmetric matrix $\Lambda$, such that the bracket of the values at $\xi$ of two sections of $L_K^k$ is the value of a section of $L_K^{3k}$, for every $k \ge 1$. It concludes that $\Lambda = 0$. The field $K$ has characteristic $0$ because $R$ contains $\mathbb{Q}$. By step 7 the lemma applies to $\delta_1$ and $\Lambda$, so $\Lambda = 0$. $\square$

The derivation $\delta_0$ is a "horizontal" direction, since it kills the base, and the $\delta_a$ are the vertical directions. The theorem says that a bracket condition of this kind leaves no room for a vertical second-order part.

**Theorem 7.21.2 (Uniqueness of the symbol).** Let $(\Omega, \varphi, x', \delta, g)$ be a framed formal point of $G$. For $j = 1, 2$ let $d_j$ be a derivation of $\operatorname{Frac} \Omega$, $\Lambda_j$ a symmetric $n \times n$ matrix, $u^{(j)} \in (\operatorname{Frac} \Omega)^n$ and $p_j, p'_j \in \operatorname{Frac} \Omega$. Let $\mathcal{H}^{(j)}_k$ be the operator $\mathcal{H}_k$ of step 5 of Section 20 for these data. Suppose that $d_1(\varphi(r)) = d_2(\varphi(r))$ for each $r \in R$, and that $\mathcal{H}^{(j)}_k$ maps $V_k$ into $V_k$ for $j = 1, 2$ and each $k \ge 1$. Then $\Lambda_1 = \Lambda_2$.

Lean: `GlobalTheory.HeatSym.symbol_unique` (also `GlobalTheory.T.heatOperator_symbol_unique_principalPolarisation`, a second name).

*Proof.* The operator $\mathcal{H}_k$ is linear in its data. So $\mathcal{Q}_k = \mathcal{H}^{(1)}_k - \mathcal{H}^{(2)}_k$ is the operator $\mathcal{H}_k$ for $d = d_1 - d_2$, $\Lambda = \Lambda_1 - \Lambda_2$, $u = u^{(1)} - u^{(2)}$, $p = p_1 - p_2$ and $p' = p'_1 - p'_2$. The matrix $\Lambda$ is symmetric, and $d$ kills $\varphi(R)$. By closure property 1, $\mathcal{Q}_k$ maps $V_k$ into $V_k$.

Let $k \ge 1$ and $b, c \in V_k$. Put $B(b, c) = \mathcal{Q}_{2k}(b c) - b\, \mathcal{Q}_k(c) - c\, \mathcal{Q}_k(b)$. By closure properties 1 and 2, $B(b, c) \in V_{2k}$. We compute $B$. In $\mathcal{Q}_{2k}(bc)$ the first term is $4k\, d(bc)$, and $b\, \mathcal{Q}_k(c) + c\, \mathcal{Q}_k(b)$ has first term $2k\, d(bc)$. The second derivatives satisfy
$$\delta_a \delta_e (b c) = b\, \delta_a \delta_e c + c\, \delta_a \delta_e b + \delta_a b\, \delta_e c + \delta_e b\, \delta_a c,$$
so with the symmetry of $\Lambda$ the terms in $\Lambda$ give $-2 \sum_{a,e} \Lambda_{ae}\, \delta_a b\, \delta_e c$. The terms in $u$ cancel by the Leibniz rule. The terms of order $0$ give $(8k^2 p + 4k p') bc - (4k^2 p + 4k p') bc$. Hence
$$B(b, c) = 2k\, d(bc) - 2 \sum_{a,e} \Lambda_{ae}\, \delta_a b\, \delta_e c + 4k^2 p\, b c.$$
Now $b\, B(b, c)$ and $c\, B(b, b)$ lie in $V_{3k}$ by closure property 2, and so does their difference by property 1. The terms in $p$ cancel, and $b\, d(bc) - c\, d(b^2) = b(b\, dc - c\, db)$ since $d(b^2) = 2 b\, db$. So
$$b\, B(b, c) - c\, B(b, b) = 2\, \beta_k(d, \Lambda; b, c).$$
By closure property 3, $\beta_k(d, \Lambda; b, c) \in V_{3k}$. The previous theorem, with $\delta_0 = d$, gives $\Lambda = 0$, that is $\Lambda_1 = \Lambda_2$. $\square$

Only the symbols are compared. The derivations $d_1$ and $d_2$, the vectors $u^{(j)}$ and the scalars $p_j, p'_j$ need not agree, and the proof does not show that they do.

**Remark 7.21.3 (Formalization).** The proofs are in [VerticalSymbolZeroOfBracketPreserving.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/VerticalSymbolZeroOfBracketPreserving.lean#L31) and [HeatOperatorSymbolUniquePrincipalPolarisation.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HeatOperatorSymbolUniquePrincipalPolarisation.lean#L26). The `T.*` names are wrappers, at line 16 and line 17 of the matching `Statement` files, that close their goal with `first | exact @X | exact X | (intros; apply X <;> assumption)`. The sets $V_k$ are `HeatSym.VS`, closure property 3 is `VS.half`, the linearity of $\mathcal{H}_k$ is `ringOp_sub` and the identity for $b\, B(b,c) - c\, B(b,b)$ is `bracket`, in [RingOpSub.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/RingOpSub.lean#L22) at lines 22, 27, 36 and 43. Closure properties 1 and 2 are the input lemmas `T.sub_of_scaled_section_values` and `T.mul_of_scaled_section_values`. The derivation $\delta_1$ of step 5 is built from its additivity and Leibniz laws with `HeatSym.derOfFun` (line 22). The other inputs are `T.exists_genericPoint_abelianVariety_through_formalPoint`, `T.generic_fibre_invariant_vectorFields_at_generic_point`, `T.polarisation_value_spaces_generic_point_dictionary`, `T.secondOrderSymbol_bracket_rescale_by_unit_pow` and `T.verticalSecondOrderSymbol_vanishes_of_polarisation`, the last a wrapper of `Heat.gc_symbol_vanishes`. They have no entries in this chapter, and we use only their statements. Both theorems take a derivation `D` of $R$ (line 26 and line 31) that no hypothesis and no conclusion mentions; `symbol_unique` passes it to `vertical_symbol_zero`, which passes it to the input lemmas. In the same way the monomial data, the abelian locus, the completeness of $\Omega$ and the fields $\partial'_a$ go only to the input lemmas. The name `heatOperator_symbol_unique_principalPolarisation` speaks of a principal polarization, but no hypothesis bounds the degree of the polarization.
