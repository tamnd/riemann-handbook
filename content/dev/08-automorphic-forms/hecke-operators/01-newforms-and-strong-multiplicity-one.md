---
title: Newforms and strong multiplicity one
decls:
  - UpperTheory.V.Af.strongMultOneReal
  - UpperTheory.V.Af.StrongMultiplicityOne.smoCentral
  - UpperTheory.V.Af.strongMultOneC
  - UpperTheory.V.Af.repNewform
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Newforms and strong multiplicity one

This section proves strong multiplicity one for cuspidal representations of $\mathrm{GL}_a$ over a totally real field and over a totally complex field, and then uses it to attach a classical newform to a cuspidal representation of $\mathrm{GL}_2$ over $\mathbb{Q}$ of cohomological weight. The totally real form is used in [the automorphy of the window](/entry/v-window-of-automorphy-csd-ss-mono-odd/). The totally complex form is used in the step [every character](/step/every-character/). The newform is used in [the twist that kills the obstruction](/entry/exists-newform-attached-twist-of-kills-mu/).

### Cuspidal representations and Satake parameters

Let $F$ be a number field, $a \ge 1$, and $G = \mathrm{GL}_a$. Let $\mathcal{S}$ be the space of smooth functions on $G(\mathbb{A}_F)$. The group $G(\mathbb{A}_{F,f})$ acts on $\mathcal{S}$ by right translation, and so do the maximal compact subgroup $K_\infty$ of $G(F \otimes \mathbb{R})$ and the Lie algebra of $G(F \otimes \mathbb{R})$ (by derivatives). A *cusp form* is an automorphic form in the sense of the Background ([automorphic forms](/learn/automorphic-forms/#automorphic-forms-on-adelic-groups)) whose constant terms along all proper parabolic subgroups vanish ([cusp forms](/learn/automorphic-forms/#constant-terms-and-cusp-forms)).

**Definition 6.1.1 (Cuspidal representation).** A *cuspidal representation* of $G$ is a nonzero subspace $V \subseteq \mathcal{S}$ of cusp forms that is stable under the three actions and is irreducible: a stable subspace $W \subseteq V$ is $0$ or $V$. Two cuspidal representations are *isomorphic* if there is a linear bijection $V \to V'$ that commutes with the three actions.

So a cuspidal representation is a subspace, not an abstract representation. Two isomorphic cuspidal representations can, a priori, be different subspaces. The totally complex theorem below gives equality of subspaces.

Let $w$ be a finite place of $F$, $F_w$ the completion and $K_w = \mathrm{GL}_a(\mathcal{O}_w)$. Restrict the action on $V$ to $\mathrm{GL}_a(F_w)$.

**Definition 6.1.2 (Satake parameter).** Let $B$ be a multiset of $a$ nonzero complex numbers. We say that $V$ *has Satake parameter $B$ at $w$* if $V$ has a nonzero $K_w$-fixed vector and every nonzero $K_w$-fixed vector of $V$ is an eigenvector of the spherical Hecke algebra at $w$ with eigenvalues given by $B$ through the Satake transform ([unramified representations](/learn/representations/#unramified-representations)).

At an infinite place $v$ the center of the enveloping algebra acts on $V$ by a character. We write it by a multiset $m$ of $a$ complex numbers: the Capelli element with parameter $u$ acts by $\prod_{z \in m} (u + z)$. We then say that $V$ *has infinitesimal character $m$ at $v$*.

### Strong multiplicity one

**Theorem 6.1.3 (Strong multiplicity one).** Let $\pi$ and $\pi'$ be cuspidal automorphic representations of $\mathrm{GL}_n(\mathbb{A}_F)$. If $\pi_w \cong \pi'_w$ for all but finitely many places $w$, then $\pi = \pi'$ as subspaces of the cusp forms.

This is the theorem of Jacquet, Piatetski-Shapiro and Shalika; see the Notes and references. We prove two forms of it. The first one is over a totally real field.

**Theorem 6.1.4 (Strong multiplicity one, totally real).** Let $F$ be totally real, $a \ge 1$, and let $\pi$, $\pi'$ be cuspidal representations of $\mathrm{GL}_a$ over $F$. Assume that for all but finitely many finite places $w$ there is a multiset $B$ such that $\pi$ and $\pi'$ both have Satake parameter $B$ at $w$. Then $\pi$ and $\pi'$ are isomorphic.

Lean: `UpperTheory.V.Af.strongMultOneReal`.

We need two tools. Let $\mathfrak{g}_\infty$ be the Lie algebra of $\mathrm{GL}_a(F \otimes \mathbb{R})$. For a smooth function $f$ on $G(\mathbb{A}_F)$ and a Schwartz function $\beta$ on $\mathfrak{g}_\infty$, the *smoothing* $f * \beta$ is the integral of the right translates of $f$ by elements near $1$ in $G(F \otimes \mathbb{R})$, weighted by $\beta$ through a fixed chart of $G(F \otimes \mathbb{R})$ at $1$. A cusp form is *central* if it is invariant under the positive real scalars $\mathbb{R}_{>0} \subset G(F \otimes \mathbb{R})$. Two central cusp forms $\varphi$, $\varphi'$ are *orthogonal under translation* if
$$\int_{G(F)^1 \backslash G(\mathbb{A}_F)^1} \overline{\varphi(xg)}\, \varphi'(xg')\, dx = 0 \quad \text{for all } g, g' \in G(\mathbb{A}_F).$$

**Lemma 6.1.5 (Pairing).** Let $U$, $U'$ be nonzero stable spaces of central cusp forms with the same Satake parameters at almost all $w$. Then there are $\varphi \in U$, $\varphi' \in U'$ and Schwartz functions $\beta$, $\beta'$ on $\mathfrak{g}_\infty$ with $\varphi * \beta = \varphi' * \beta' \ne 0$.

This is the core of the classical proof. Write $\varphi$ and $\varphi'$ by their Whittaker expansions ([Fourier coefficients and Whittaker functions](/learn/automorphic-forms/#fourier-coefficients-and-whittaker-functions)). At almost all $w$ the local Whittaker functions of the spherical vectors are equal, since the Satake parameters are equal. At the finitely many other places one uses the Kirillov model to choose vectors with the same Whittaker function, and the smoothing at infinity does the same for the archimedean places. We take the lemma in this form as an input; see the Remark.

**Lemma 6.1.6 (Orthogonal smoothings vanish).** If $\varphi$ and $\varphi'$ are central cusp forms that are orthogonal under translation, and $\varphi * \beta = \varphi' * \beta'$, then $\varphi * \beta = 0$.

The common function $\psi = \varphi * \beta$ lies in the closed span of the translates of $\varphi$ and also in that of $\varphi'$. Since the two spans are orthogonal, $\psi$ is orthogonal to itself.

*Proof of the theorem.* There is a Hecke character $\chi$ such that $\pi \otimes \chi$ is central. Twisting by $\chi$ keeps the equality of Satake parameters at almost all $w$, and an isomorphism $\pi \otimes \chi \cong \pi' \otimes \chi$ gives $\pi \cong \pi'$. So we may assume that $\pi$ is central. The central character of $\pi'$ agrees with that of $\pi$ at almost all places, so $\pi'$ is central too. Assume that $\pi$ and $\pi'$ are not isomorphic. Then their spaces are orthogonal in $L^2(G(F)^1 \backslash G(\mathbb{A}_F)^1)$, so all their elements are orthogonal under translation. The pairing lemma gives $\varphi$, $\varphi'$, $\beta$, $\beta'$ with $\varphi * \beta = \varphi' * \beta' \ne 0$, and the second lemma gives $\varphi * \beta = 0$. This is a contradiction. $\square$

The totally complex form gives equality of subspaces. It is proved through a statement on stable spaces of central cusp forms. Here a space $U$ of cusp forms is *stable* if it is stable under the three actions, and *irreducible* if it is nonzero and has no stable subspaces other than $0$ and $U$. We say that $U$ *has Satake parameter $B$ at $w$* if every $K_w$-fixed element of $U$ is a Hecke eigenfunction at $w$ with parameter $B$.

**Lemma 6.1.7 (Strong multiplicity one, central case).** Let $E$ be totally complex, $n \ge 1$, and let $U$, $U'$ be irreducible stable spaces of cusp forms on $\mathrm{GL}_n(\mathbb{A}_E)$. Assume that $U$ consists of central forms and that $U$ and $U'$ have the same Satake parameter at all but finitely many $w$. Then $U = U'$.

Lean: `UpperTheory.V.Af.StrongMultiplicityOne.smoCentral`.

*Proof.* As in the totally real case, $U'$ is central. The intersection $U \cap U'$ is stable. Since $U'$ is irreducible, either $U \cap U' = U'$ or $U \cap U' = 0$. In the first case $U' \subseteq U$, and $U' = U$ since $U$ is irreducible. In the second case, take an orthogonal stable complement $C$ of $U$ in the central cusp forms. Then $U' \subseteq U \oplus C$, and the projection of $U'$ to $C$ gives a nonzero stable space $D \subseteq C$ with the same Satake parameters as $U$. The pairing lemma for $U$ and $D$ gives $\varphi * \beta = \varphi' * \beta' \ne 0$ with $\varphi \in U$, $\varphi' \in D$. But $U \perp D$, so the forms are orthogonal under translation, and the second lemma gives $\varphi * \beta = 0$. This is a contradiction. $\square$

**Theorem 6.1.8 (Strong multiplicity one, totally complex).** Let $E$ be totally complex, $n \ge 0$, and let $\pi$, $\pi'$ be cuspidal representations of $\mathrm{GL}_n$ over $E$ that have the same Satake parameter at all but finitely many finite places. Then $\pi$ and $\pi'$ are the same subspace of the cusp forms.

Lean: `UpperTheory.V.Af.strongMultOneC`.

*Proof.* Twist $\pi$ by a Hecke character $\chi$ that makes it central. A cuspidal representation is an irreducible stable space of cusp forms, and at a place where $\pi$ has Satake parameter $B$, every spherical vector is an eigenfunction with parameter $B$. So the lemma applies to the twists of $\pi$ and $\pi'$ and gives their equality. Twisting back gives $\pi = \pi'$. $\square$

### The newform attached to a representation

Let $k \ge 2$ and $M \ge 1$. Let $S_k(\Gamma_1(M))$ be the space of cusp forms of weight $k$ for $\Gamma_1(M)$ ([modular forms](/learn/automorphic-forms/#modular-forms)), and write $f = \sum_{n \ge 1} a_n q^n$.

**Definition 6.1.9 (Newform).** A *newform* of weight $k$ is a level $M \ge 1$, a Dirichlet character $\chi$ modulo $M$ and a form $f \in S_k(\Gamma_1(M))$ with character $\chi$ such that $a_1 = 1$, and for each prime $p \nmid M$ there is $\lambda_p$ with
$$a_{pn} + \chi(p)\, p^{k-1} a_{n/p} = \lambda_p\, a_n \quad \text{for all } n \ge 1$$
(with $a_{n/p} = 0$ if $p \nmid n$), and $f$ is *new*: if $M' \mid M$, $M' \ne M$, and $g$ is a cusp form of weight $k$, level $M'$ and some character whose Hecke eigenvalues equal $a_p(f)$ at all but finitely many $p$, then $g = 0$. The *Hecke polynomial* of $f$ at $p \nmid M$ is
$$H_p(X) = X^2 - a_p X + \chi(p)\, p^{k-1}.$$

The roots of $H_p$ are the classical Satake parameters of $f$ at $p$. For an integer $j$ and a multiset $B$ of two numbers, put $p^{1/2} B = \{p^{1/2} b : b \in B\}$.

**Theorem 6.1.10 (Newform of a cuspidal representation).** Let $k \ge 2$, $j \in \mathbb{Z}$, and let $\pi$ be a cuspidal representation of $\mathrm{GL}_2$ over $\mathbb{Q}$ with infinitesimal character $\{\tfrac12 + j,\ \tfrac32 - k + j\}$ at the real place. Then there is a newform $f$ of weight $k$ and level $M$ such that for every prime $p \nmid M$ there is $B$ with $\pi$ of Satake parameter $B$ at $p$ and
$$\prod_{b \in p^{1/2} B} \bigl(X - p^{j} b\bigr) = H_p(X).$$

Lean: `UpperTheory.V.Af.repNewform`.

*Proof.* Twist $\pi$ by a power of the norm to get $\pi_0$ with infinitesimal character $\{\tfrac{k-1}{2}, -\tfrac{k-1}{2}\}$. This is the infinitesimal character of the discrete series of weight $k$, so $\pi_0$ has a nonzero lowest weight vector of weight $k$. This vector is a holomorphic cusp form $g$ of weight $k$ and some level $N$. It is a Hecke eigenform with $a_p(g) = p^{(k-1)/2}(\alpha + \beta)$ and $\alpha\beta = \chi_g(p)$ at almost all $p$, where $\{\alpha, \beta\}$ is the Satake parameter of $\pi_0$. By Atkin-Lehner theory, $g$ has the same eigenvalues at almost all $p$ as a newform $f$. To compare the characters of $f$ and $g$ we use the Rankin-Selberg method ([Rankin-Selberg integrals](/learn/trace-formula/#rankin-selberg-integrals)): two eigenforms with equal $a_p$ at almost all $p$, and with $\overline{a_p}\,\chi(p) = a_p$ for both, have equal characters at almost all $p$. So the Hecke polynomial of $f$ equals the twisted Satake polynomial of $\pi$ at almost all $p$. Now $f$ gives a cuspidal representation $\pi_f$ of $\mathrm{GL}_2$ over $\mathbb{Q}$ whose Satake parameter at each $p \nmid M$ is read off from $H_p$. The totally real form of strong multiplicity one gives $\pi_f \cong \pi$, so the equality holds at every $p \nmid M$. A monic polynomial determines its multiset of roots, which gives $B$. $\square$

**Remark 6.1.11 (Formalization).** The totally real theorem is reduced to seven inputs in [ExistsCombComb.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/AutomorphicForms/SmoothRepresentationsGL/ExistsCombComb.lean#L417): the twist to a central form, the twist reduction, the central character, the pairing lemma, the orthogonality of non-isomorphic representations, orthogonality under translation, and the vanishing of orthogonal smoothings. The pairing lemma is assembled from statements on Kirillov models and Whittaker functions whose proofs we did not unfold, and we did not unfold the chart used in the smoothing. In the totally complex theorem the hypothesis $1 \le n$ of the central lemma is not asked; the case $n = 0$ is handled apart. The definition of "$U$ has Satake parameter $B$ at $w$" for a stable space only asks that $K_w$-fixed vectors are eigenvectors; it holds vacuously if $U$ has no such vector. The Atkin-Lehner step and the Rankin-Selberg step are the inputs `MinNew` and `CharEq2` ([RnStmt.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/GaloisLibrary/CrystallineBaseChange/RnStmt.lean#L103), [StripInt.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/AutomorphicForms/AutomorphicRankinSelberg/StripInt.lean#L201)).
