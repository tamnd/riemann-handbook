---
title: Eisenstein congruences and unitary seeds in rank three
decls:
  - UpperTheory.V.Z.Sym.Unl.half_of_printed_hida
  - UpperTheory.V.Sd.EG.core
  - UpperTheory.V.Z.Sym.W.prop_eg_complex_of_printed_hida
  - UpperTheory.V.Z.Sym.W.prop_eg_w_of_printed_hida
  - UpperTheory.V.Z.Sym.W.seedInW_alt
  - UpperTheory.V.Z.Sym.W.unitary_three_automorphy_dense_of_prints_and_row
  - UpperTheory.V.Z.Sym.W.unitary_three_automorphy_dense_of_prints
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Eisenstein congruences and unitary seeds in rank three

The three-dimensional unitary automorphy statement of section 1 asks for seeds: irreducible three-dimensional representations of $G_L$ of large weight, with a prescribed residual shape, that are automorphic. We build them as adjoints. An Eisenstein congruence gives a modular two-dimensional $\rho$ of $G_{\mathbb{Q}}$ that is congruent to a sum of two characters. Then $\operatorname{ad}^0 \rho|_{G_L}$ has the shape $(\varphi, 1, \varphi^{-1})$ residually, and [adjoint automorphy](/entry/adjoint-automorphy-w-of-pure-weight-adjoint-lift/) makes it automorphic. The work of this section is to control the Frobenius eigenvalues of $\rho$ well enough that the adjoint is unlinked, and to twist $\rho|_{G_L}$ so that the previous section applies.

Let $l$ be an odd prime, $\iota \colon \overline{\mathbb{Q}}_l \to \mathbb{C}$ an isomorphism, $c$ a complex conjugation and $\varepsilon$ the cyclotomic character.

**Definition 8.14.1 (Unlinked).** A representation $r$ of $G_L$ is unlinked if at each finite place $w \nmid l$ where $r$ has finite image of inertia, there are $j \ge 1$ and a Frobenius element $s$ for $N(w)^j$ such that no two eigenvalues $\alpha$, $\beta$ of $r(s)$ satisfy $\alpha^k = (N(w)^j \beta)^k$ for some $k \ge 1$.

**Definition 8.14.2 (No half step).** A two-dimensional $\rho$ has no half step if for each prime $p \ne l$, each Frobenius element $s$ at $p$ and all eigenvalues $\alpha, \beta$ of $\rho(s)$, we have $|\iota\alpha|^2 \ne p\,|\iota\beta|^2$.

**Proposition 8.14.3 (No half step for ordinary eigenforms).** Assume the extended hypotheses. Let $k \ge 3$, $N \ge 1$, $\chi$ a primitive Dirichlet character modulo $N$, and $g$ a normalized eigenform of weight $k$, level $\Gamma_1(N)$ and character $\chi$ with eigenvalues $a_p$, such that each conjugate $\sigma(g)$, $\sigma \in \operatorname{Aut}(\mathbb{C})$, is a cusp form of character $\sigma \circ \chi$. Let $r$ be an ordinary representation attached to the cuspidal $\pi$ of $g$, with $\det r = \varepsilon^{k-1} \xi$ for a finite order $\xi$. Then $r$ has no half step.

Lean: `UpperTheory.V.Z.Sym.Unl.half_of_printed_hida`.

*Proof.* Suppose $|\iota x|^2 = p\,|\iota y|^2$ for two eigenvalues of $r(s)$. If $p \mid N$, then $|a_p|^2 = p^{k-1}$, and one eigenvalue of $r(s^{-1})$ has absolute value $|a_p|$. The determinant has absolute value $p^{k-1}$, since $\xi$ has finite order. So both eigenvalues have the same absolute value, and $p = 1$, which is false. If $p \nmid N$, the characteristic polynomial of $r(s^{-1})$ is $X^2 - a_p X + \chi(p) p^{k-1}$. If $x = y$ we get $p = 1$ again. Otherwise its two roots satisfy $|\alpha|^2 = p\,|\beta|^2$. Take $\sigma \in \operatorname{Aut}(\mathbb{C})$ with $\sigma(\sqrt p) = -\sqrt p$. The relation $\overline{a_p}\chi(p) = a_p$ holds for $g$ and for $\sigma(g)$, and the two root equations together give a contradiction. $\square$

**Lemma 8.14.4 (From an Eisenstein eigenform to Galois).** Assume the extended hypotheses. Let $g$ be an eigenform of weight $k \ge 3$, level $Mw$ and character $\chi = \varphi_0\theta_0$, with the conjugation condition, such that $a_p(g) \equiv 1 + \chi(p)p^{k-1}$ modulo the maximal ideal for each prime $p$. Then there is a continuous $\rho \colon G_{\mathbb{Q}} \to \mathrm{GL}_2(\overline{\mathbb{Q}}_l)$ that is irreducible and modular, with $\det \rho = \varepsilon^{k-1}\varphi\theta$, residually a sum $1 \oplus \varepsilon^{k-1}\varphi$, of type given by $1$ and $\varphi\theta$ away from $l$, ordinary above $l$ with weights $k - 1, 0$, attached to a regular algebraic cuspidal $\pi$, with $|\iota\alpha| < N(v)\,|\iota\beta|$ for any two Frobenius eigenvalues at $v \nmid l$, and with no half step.

Lean: `UpperTheory.V.Sd.EG.core`.

*Proof.* The extended hypotheses give an ordinary representation $r$ attached to $g$. Let $\rho$ be the twist of $r$ by $\varepsilon^{k-1}\varphi\theta$. The congruence of $a_p(g)$ gives the residual sum, and the local properties of $r$ give the type and ordinarity. The bound on eigenvalues comes from the ordinary window of the Hida family of $g$. The proposition gives no half step for $r$. A twist by a character keeps both eigenvalue conditions. $\square$

**Theorem 8.14.5 (Eisenstein congruences).** Assume the extended hypotheses. Let $N > 0$ with $l \nmid N$, let $w \nmid N$ be prime, let $\theta \ne 1$ be a character of $G_{\mathbb{Q}}$ with $\theta^l = 1$ that is trivial on the elements fixing the $w$-th roots of unity, and let $\varphi \ne 1$ be a character that is trivial on the elements fixing the $N$-th roots of unity and on the Frobenius elements at $w$. Then there is $k_0$ such that for each $k \ge k_0$ with $\varphi(c) = (-1)^k$ there is $\rho$ with the properties of the lemma.

Lean: `UpperTheory.V.Z.Sym.W.prop_eg_complex_of_printed_hida`.

*Proof.* Write $\varphi$ as the Galois character of a primitive Dirichlet character $\varphi_0$ of conductor $M \mid N$, and $\theta$ as that of a character $\theta_0$ modulo $w$. Then $M > 1$, $\theta_0$ has order $l$, so $l \mid w - 1$, and $\varphi_0(w) = 1$. Let $\chi = \varphi_0\theta_0$. By the existence of eigenforms congruent to Eisenstein series (a result proved in an earlier chapter from the $q$-expansion of the Eisenstein series of character $\chi$), there is $k_0$ such that for $k \ge k_0$ with $\varphi_0(-1) = (-1)^k$ there is an eigenform $g$ as in the lemma. Take $k \ge \max(k_0, 3)$ and apply the lemma. $\square$

**Corollary 8.14.6 (Unlinked adjoints).** Under the same assumptions, $\rho$ can be chosen with $\operatorname{ad}^0 \rho$ unlinked.

Lean: `UpperTheory.V.Z.Sym.W.prop_eg_w_of_printed_hida`.

*Proof.* Let $\alpha$, $\beta$ be the eigenvalues of $\rho(s)$. The eigenvalues of $\operatorname{ad}^0 \rho(s)$ are $\alpha/\beta$, $1$ and $\beta/\alpha$. A relation $(\alpha/\beta)^k = (N(w)^j)^k$ or a relation between $1$ and $\alpha/\beta$ forces $|\iota\alpha| = N(w)^j |\iota\beta|$, $|\iota\alpha|^2 = N(w)^j |\iota\beta|^2$ or $|\iota\alpha| = |\iota\beta|$ up to the factor $N(w)^j$. The eigenvalue bound excludes the first, and no half step excludes the second. $\square$

**Proposition 8.14.7 (Twisting to a unitary seed).** Assume the extended hypotheses. Let $K$ be imaginary quadratic and $L \supseteq K$ a CM field abelian over $\mathbb{Q}$, with the characters $\chi'$, $\eta$, $\theta$ and a level $M$ as in the seed statement. Let $\rho$ be a two-dimensional representation of $G_{\mathbb{Q}}$ as in the corollary, with $\det \rho = \varepsilon^m \chi'\eta\theta$ and $\operatorname{ad}^0 \rho$ unlinked. Then there is a character $\kappa$ of $G_L$ such that $\rho|_{G_L} \otimes \kappa$ is continuous and conjugate self-dual automorphic, has a symplectic pairing for every complex conjugation, stays irreducible on open subgroups, is trivial on inertia at places prime to $M$, is potentially ordinary above $l$, and has unlinked adjoint.

Lean: `UpperTheory.V.Z.Sym.W.seedInW_alt`.

*Proof.* Put $\Theta = \chi'\eta\theta$. Then $\theta(c) = 1$, as $\theta$ has odd order $l$, so $\Theta(c) = (-1)^{m+1}$. The existence of twisting characters gives $\kappa$ with $\kappa(s)\kappa(cs c^{-1}) \det \rho(s) = \varepsilon(s)^{-1}$, unramified at places prime to $M$ and with prescribed shape above $l$. This identity makes the twist conjugate self-dual with multiplier $\varepsilon^{-1}$. Base change from $\mathbb{Q}$ to $K$, which is quadratic, and from $K$ to $L$, which is abelian and so solvable, makes $\rho|_{G_L}$ automorphic. Twisting by $\kappa$ keeps automorphy. The adjoint does not see a twist by a character, so $\operatorname{ad}^0$ of the twist is $\operatorname{ad}^0 \rho|_{G_L}$, which is unlinked. $\square$

**Theorem 8.14.8 (Unitary automorphy in rank three).** Assume the extended hypotheses and the Galois row. Let the field pair $K \subseteq L$, the characters $\chi' \ne \eta$, $\theta$, the integers $N$, $w$, $j$ and the level $M$ with $2l \mid M$ satisfy the seed conditions. Then for each $B$ there are $m \ge B$ with $m \equiv j \pmod{l - 1}$ and an irreducible $r \colon G_L \to \mathrm{GL}_3(\overline{\mathbb{Q}}_l)$ that is a seed with residual characters $(\varepsilon^j\chi', 1, (\varepsilon^j\chi')^{-1})$, weights $(m, 0, -m)$ and twist $\varepsilon^{-1}$. The same holds under the extended hypotheses alone.

Lean: `UpperTheory.V.Z.Sym.W.unitary_three_automorphy_dense_of_prints_and_row` (also `UpperTheory.V.Z.Sym.W.unitary_three_automorphy_dense_of_prints`, the form that takes the Galois row from the extended hypotheses).

*Proof.* Let $\varphi = \chi'\eta$. Then $\eta^2 = 1$ and $\eta(c) = -1$, so $\varphi$ is trivial at $N$ and $w$ in the required sense, and $\varphi \ne 1$ since $\chi' \ne \eta$. Take $m = j + (l - 1)t$ with $t$ large, so that $m \ge B$, $m \equiv j$ and $\varphi(c) = (-1)^{m+1}$. The corollary at weight $m + 1$ gives $\rho$. Let $r = \operatorname{ad}^0 \rho|_{G_L}$. It is irreducible, has a symmetric pairing, and has the right shape away from $l$ and above $l$, because $\rho$ does. For automorphy, the twisting proposition gives $\kappa$, adjoint automorphy gives the automorphy of $\operatorname{ad}^0(\rho|_{G_L} \otimes \kappa) \otimes \varepsilon^{-1}$, and the twist by $\kappa$ disappears in the adjoint. $\square$

**Remark 8.14.9 (Formalization).** The lemma `UpperTheory.V.Sd.EG.core` is private, in [WEGCore.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/WEGCore.lean#L129), so no other file can call it. The proof of the half step proposition in [THalfOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/THalfOf.lean#L54) is a line by line copy of `halfOf` in HalfOf.lean, with the extended hypotheses in place of the hypotheses H, and its private helpers are copied too. In [UnitaryThreeInputsOfLiterature.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/UnitaryThreeInputsOfLiterature.lean#L30), the form without the Galois row calls the other one with `rowOf' hH.litN.aut.gal`, and `rowOf'` is the identity, so the row is a field of the extended hypotheses. The twisting proof in [TSeedInW.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TSeedInW.lean#L117) raises `maxHeartbeats` to 1600000 for one theorem. We have not unfolded the seed predicate `IsSeedAlt` or the field pair conditions.
