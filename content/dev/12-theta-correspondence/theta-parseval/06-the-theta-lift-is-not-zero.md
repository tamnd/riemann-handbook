---
title: The theta lift is not zero
decls:
  - UpperTheory.TP.tools_holds_k
  - UpperTheory.TP.tLift_of_tools_k
  - UpperTheory.TP.tLift_holds_k
  - UpperTheory.TP.K.tLiftK
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The theta lift is not zero

This section proves the main result of the chapter: in the stable range, the global [theta lift](/learn/theta/#the-global-theta-lift) from a definite [[unitary group|0R9R0Y1HDK]] $U(n)$ to a definite unitary group $U(d)$ sends each automorphic representation of $U(n)$ with large enough weights to a nonzero automorphic representation of $U(d)$, with the expected weights at the infinite places and the expected local components at the split places. The proof is the classical one of Rallis and Li. The [Rallis inner product formula](/learn/theta/#the-rallis-inner-product-formula) writes the norm of the lift as an integral of a product of two matrix coefficients, one of the Weil representation and one of the automorphic representation. The test vectors of [the previous section](/entry/real-pair-k/) make this integral a main term plus a small tail, and so it is not zero. The inner product formula comes from the [Siegel-Weil formula for a definite space](/entry/siegel-weil-std-k/) and the [doubling method](/learn/theta/#the-doubling-method).

We keep the notation of [the Weil representation of a good unitary pair](/entry/exists-is-weil-k/): $E$ is a CM field with maximal real subfield $F$, $X$ is a definite Hermitian space of dimension $n$ with Gram matrix $1$, $W$ is a definite skew-Hermitian space of dimension $d$ with Gram matrix $\delta \cdot 1$, and $\omega$ is the Weil representation of $U(X)(\mathbb{A}) \times U(W)(\mathbb{A})$ on the [[Schwartz space|GE020MY43M]] of $n \times d$ matrices over $\mathbb{A}_E$, made with splitting characters $\chi_X$ and $\chi_W$. The theta kernel of $\Phi$ is $\theta(\Phi)(g, h) = \sum_{x} \omega(g, h)\Phi(x)$, the sum over the rational $n \times d$ matrices (see [theta kernels](/learn/theta/#theta-kernels)). Let $\mathcal{D}$ be a fundamental domain for $U(X)(F)$ in $U(X)(\mathbb{A})$ with a Haar measure $dg$; since $X$ is definite, $U(X)(F) \backslash U(X)(\mathbb{A})$ is compact.

**Definition 6.6.1 (Theta lift and matrix coefficients).** For a Schwartz function $\Phi$ and a function $\varphi$ on $U(X)(\mathbb{A})$ the *theta lift* is the function on $U(W)(\mathbb{A})$
$$\Theta(\Phi, \varphi)(h) = \int_{\mathcal{D}} \theta(\Phi)(g, h)\, \overline{\varphi(g)}\, dg.$$
The *Weil coefficient* of $\Phi$ is $c_\Phi(g) = \langle \omega(g, 1)\Phi, \Phi \rangle$, the $L^2$ pairing on the Schwartz space. The *automorphic coefficient* of $\varphi$ is $m_\varphi(g) = \int_{\mathcal{D}} \varphi(yg)\, \overline{\varphi(y)}\, dy$. A *polynomial datum* is a finite sum of pure tensors $f \otimes \bigotimes_v \phi_v$, where $f$ is in the polynomial Fock space at the infinite places, each $\phi_v$ is Schwartz-Bruhat, and $\phi_v$ is the vacuum vector for almost all $v$.

The proof uses fourteen facts about theta kernels and Eisenstein series for the good base data of this chapter. They are the *tools*.

**Proposition 6.6.2 (The tools).** For good base data the following hold:

1. the full [Siegel-Weil formula](/learn/theta/#the-siegel-weil-formula) for the doubled space, in the definite case;
2. the box sections: the sections of the doubled Weil representation made from $\Phi_1 \otimes \bar\Phi_2$ are standard sections of the [Siegel Eisenstein series](/learn/automorphic-forms/#siegel-eisenstein-series);
3. the doubling identity $\theta(\Phi_1)(g, h)\, \overline{\theta(\Phi_2)(g', h)} = \chi_W(\det g')^{-1}\, \theta_2(\Phi_1 \otimes \bar\Phi_2)(\iota(g, g'), h)$ for the doubled pair;
4. the stabilizer $K$ of the doubled lattice is compact;
5. $U(Y)(F) \backslash U(Y)(\mathbb{A})$ is compact for each definite space $Y$;
6. the theta kernel is continuous and automorphic in both variables;
7. polynomial data are Schwartz functions;
8. the unfolding of the open orbit for the doubled Eisenstein series;
9. a Weil datum and a Weil representation exist for each pair of Hecke characters with the right restrictions;
10. at a place that splits in $E$, the Weil representation is the linear model of $GL_n \times GL_d$;
11. at a finite place where $\chi$ is unramified, the vacuum vector is fixed by the stabilizer;
12. the local Weil representation at each finite place exists, and fixes each Schwartz-Bruhat vector on an open set;
13. and 14. the first and second order formulas for the action of the Lie algebra on the Fock model at the real places.

Lean: `UpperTheory.TP.tools_holds_k`.

*Proof.* The Siegel-Weil formula of item 1 comes from [the Siegel-Weil formula for a definite space](/entry/siegel-weil-std-k/) with the frame and level lemmas and item 4; the pair of item 9 comes from [the existence of the Weil representation](/entry/weil-ex-k/) and a model lemma; the Lie formulas of items 13 and 14 come from the local lift and the derivative lemmas; the other items are earlier results for the good base data. $\square$

**Lemma 6.6.3 (Main term against tail).** Let $A$, $B$, $C$ be $\sigma$-finite measure spaces, let $H \subseteq B$ be measurable with $0 < \mu_B(H) < \infty$, and let $K \subseteq C$ be measurable with $\mu_C(K) < \infty$. Let $f$ be integrable on $A \times B \times C$, and let $m$, $s$, $c_0$, $w$ be functions with values in $\mathbb{C}$, $\mathbb{C}$, $\mathbb{C}$ and $[0, \infty]$, $\kappa \ne 0$ and $r > 0$, such that:

1. $f(x, b, c) = 0$ for $b \notin H$, and $f(x, b, c) = s(c)\, m(x, c)$ for $b \in H$;
2. $\int_A m(x, c)\, dx = \kappa\, c_0(c)$ for all $c$;
3. $s(c) = 1$ and $c_0(c) = r$ for $c \in K$, and $\lvert c_0(c) \rvert \le r$ and $\lvert s(c) \rvert \le w(c)$ for all $c$;
4. $\int_{C \setminus K} w\, d\mu_C < \mu_C(K)$.

Then $\int f \ne 0$.

Lean: `UpperTheory.TP.absNe`.

*Proof.* By Fubini and conditions 1 and 2, $\int f = \mu_B(H)\, \kappa \int_C s(c)\, c_0(c)\, dc$. By condition 3 the integral over $K$ is $r\,\mu_C(K)$, and the integral over $C \setminus K$ has absolute value at most $r \int_{C \setminus K} w$, which is less than $r\,\mu_C(K)$ by condition 4. So $\int_C s\, c_0 \ne 0$, and $\int f \ne 0$ because $\mu_B(H) \ne 0$ and $\kappa \ne 0$. $\square$

**Theorem 6.6.4 (Non-vanishing for a test vector).** Assume $2n \le d$, and let $t_0$ be such that the height $a(g)^t$ of the doubled group is integrable on $U(X)(\mathbb{A})$ for all $t \ge t_0$, with $t_0 < d/2$. Let $U$ be an automorphic representation of $U(n)$, and let $f_0 \ne 0$ in the polynomial Fock space and $\varphi \ne 0$ in $U$ be images of one vector of an irreducible $K_\infty$-type. Then there are Schwartz-Bruhat functions $\phi_v$, equal to the vacuum for almost all $v$, with $\Theta(f_0 \otimes \bigotimes_v \phi_v, \varphi) \ne 0$.

Lean: `UpperTheory.TP.nonVan_k`.

*Proof.* The coefficient $m_\varphi$ satisfies $\lvert m_\varphi(g) \rvert \le m_\varphi(1) = r > 0$, and $\varphi$ is fixed by an open subgroup $N$ of $U(X)(\mathbb{A})$. Choose a finite set $S_0$ of finite places such that each element that is $1$ at the places in $S_0$ and integral elsewhere is in $N$, and let $R$ be the finite set of places where $\chi_W$ is ramified. The tail estimate for the height with $t = d/2$ gives a finite set $S \supseteq S_0 \cup R$ with
$$\int_{c\ \text{not integral}} a(c)^{d/2}\, dc < \operatorname{vol}\{c\ \text{integral}\},$$
the integrals over the group $U(X)^{S}$ of elements that are $1$ at the infinite places and at $S$. At each $v \in S$ take a [bump](/entry/bump-any-k/) $(H_v, \phi_v)$ with $H_v \subseteq N$, and take the vacuum at $v \notin S$. Put $\Phi = f_0 \otimes \bigotimes_v \phi_v$.

The group $U(X)(\mathbb{A})$ is the product of the compact group $U(X)_\infty$, the group $U(X)_S$ of the places in $S$, and $U(X)^S$, as a topological group and with Haar measures. On it the integrand $c_\Phi\, \overline{m_\varphi}$ has the form of the lemma, with $H$ the group generated by the $H_v$ and $K$ the integral elements of $U(X)^S$. The coefficient $c_\Phi$ vanishes at $x b c$ for $b \notin H$, by the separation property of the bumps. For $b \in H$ it is $s(c)\, c_\Phi(x)$ with $\lvert s(c) \rvert = a(c)^{d/2}$ and $s(c) = 1$ for integral $c$, by the invariance of the bumps and of the vacuum. Since $H \subseteq N$ fixes $\varphi$, $m_\varphi(xbc) = m_\varphi(xc)$. The *Schur step*, the orthogonality relations for the compact group $U(X)_\infty$ applied to the $K_\infty$-type of $f_0$ and $\varphi$, gives $\kappa \ne 0$ with
$$\int_{U(X)_\infty} c_\Phi(x)\, \overline{m_\varphi(xc)}\, dx = \kappa\, c_\Phi(1)\, \overline{m_\varphi(c)}.$$
For integral $c$ we have $c \in N$, so $m_\varphi(c) = r$. The lemma with $w(c) = a(c)^{d/2}$ gives $\int c_\Phi\, \overline{m_\varphi} \ne 0$. By the Rallis identity below, $\Theta(\Phi, \varphi) = 0$ would force this integral to be $0$. $\square$

The Rallis identity is the input that connects the lift with the coefficients.

**Proposition 6.6.5 (Rallis inner product identity).** Assume $1 \le d$ and $t_0 < d/2$ as above. For each polynomial datum $\Phi$ and each continuous function $\varphi$ on $U(X)(F) \backslash U(X)(\mathbb{A})$, the function $c_\Phi\, \overline{m_\varphi}$ is integrable on $U(X)(\mathbb{A})$, and if $\Theta(\Phi, \varphi) = 0$ then $\int_{U(X)(\mathbb{A})} c_\Phi(g)\, \overline{m_\varphi(g)}\, dg = 0$.

Lean: `UpperTheory.TP.rallis_k`.

*Proof.* Integrability comes from a bound of $c_\Phi$ by powers of the height, the integrability of $a^t$ for $t \ge t_0$, and $t_0 < d/2$. For the second part, the norm of $\Theta(\Phi, \varphi)$ over $U(W)(F) \backslash U(W)(\mathbb{A})$ is a double integral over $\mathcal{D} \times \mathcal{D}$ of $\overline{\varphi(g)}\varphi(g')$ against the integral over $U(W)$ of $\theta(\Phi)(g, h)\overline{\theta(\Phi)(g', h)}$. By the doubling identity (tool 3) this inner integral is a theta integral for the doubled pair, and by the Siegel-Weil formula (tool 1) it is the value at $s_0 = (d - n)/2$ of a Siegel Eisenstein series on $\iota(g, g')$, made from the box section of $\Phi \otimes \bar\Phi$ (tool 2). On the diagonal $\iota(1, g)$ this section is a nonzero multiple of $c_\Phi(g^{-1})$, and the unfolding of the open orbit turns the double integral of the Eisenstein series against $\overline{\varphi} \otimes \varphi$ into $\int c_\Phi\, \overline{m_\varphi}$, as in the doubling method of Gelbart, Piatetski-Shapiro and Rallis (1987). $\square$

This is the standard [Rallis inner product formula](/learn/theta/#the-rallis-inner-product-formula) (Rallis 1984; Kudla and Rallis 1994; Gan, Qiu and Takeda 2014), here in the convergent range and in the weak form that the formal proof needs.

**Theorem 6.6.6 (Theta lift in the stable range).** Let $E$ be a CM field with good base data, let $n \ge 1$, and let $X$ be a definite Hermitian space of dimension $n$ with Gram matrix $1$. There is $d_0$ such that for all $d \ge d_0$ the following holds. Let $W$ be a definite skew-Hermitian space of dimension $d$ with Gram matrix $\delta \cdot 1$, let $\chi_X$ and $\chi_W$ be Hecke characters of $E$ with restrictions $\eta^n$ and $\eta^d$ to $\mathbb{A}_F^\times$ and exponents $m_X$ and $m_W$, and let $U$ be an automorphic representation of $U(n)$ with weight $\lambda_w$ at each infinite place $w$, such that $d + m_{W,w} \le 2\lambda_{w,k}$ for all $w$ and $k$. Then there is an automorphic representation $U'$ of $U(d)$ such that:

1. at each infinite place $w$ the representation $U'$ has a weight $\lambda'_w$ that is a lift weight of $\lambda_w$;
2. at each place $v$ of $F$ that splits in $E$, for all local components $\tau$ of $U$ and $\tau'$ of $U'$ there is a nonzero map $\beta$ from the local Schwartz space to the conjugate-linear maps $\tau \to \tau'$ that is equivariant for the Weil representation of $GL_n(F_v) \times GL_d(F_v)$.

Lean: `UpperTheory.TP.tLift_holds_k` (also `UpperTheory.TP.K.tLiftK`, the same statement under a second name).

This is the global non-vanishing of theta lifts in the stable range (Li 1992; for unitary groups also Rallis 1984). Part 2 says that $U'$ is the theta lift of $U$ at the split places, where the dual pair is $(GL_n, GL_d)$.

**Theorem 6.6.7 (The lift from the tools).** The tools and the existence of a height on the doubled group imply the theorem on the theta lift in the stable range.

Lean: `UpperTheory.TP.tLift_of_tools_k`.

*Proof.* The height gives $t_0$ such that $a^t$ is integrable for $t \ge t_0$. Choose an integer $N > 2t_0$ and put $d_0 = \max(N, 2n)$. Let $d \ge d_0$; then $2n \le d$ and $t_0 < d/2$. Since $W$ is definite, $\delta \ne 0$. Tool 9 gives a Weil datum and the Weil representation $\omega$ for $\chi_X$ and $\chi_W$, and fixed isomorphisms identify $U(X)$ and $U(W)$ with the standard groups $U(n)$ and $U(d)$. [Real test vectors](/entry/real-pair-k/) give $f_0 \ne 0$ and $\varphi \ne 0$ in one $K_\infty$-type, and at each $w$ a lift weight $\lambda'_w$ whose $U(d)$-type contains $f_0$. The non-vanishing theorem gives $\Phi = f_0 \otimes \bigotimes_v \phi_v$ with $\Theta(\Phi, \varphi) \ne 0$.

The lift map $\Phi, \varphi \mapsto \Theta(\Phi, \varphi)$ is linear in $\Phi$, conjugate-linear in $\varphi$, sends automorphic forms to automorphic forms, and is equivariant: $\Theta(\omega(g, h)\Phi, \varphi(\cdot\, g)) = \Theta(\Phi, \varphi)(\cdot\, h)$. A nonzero automorphic form on $U(d)$ has a nonzero equivariant projection $\mathrm{pr}$ onto an automorphic representation $U'$; this is the decomposition of the space of [[automorphic form|68SJQEC11F]] on a compact quotient into irreducible pieces. The equivariance of $\Theta$ and of $\mathrm{pr}$, with the abstract isotypic lemma for an irreducible representation of a subgroup, reads off the two properties from $\mathrm{pr}\,\Theta(\Phi, \varphi) \ne 0$: the $U(d)$-type of $f_0$ at $w$ occurs in $U'$, so $\lambda'_w$ is a weight of $U'$; and at a split place the map $\Phi_v \mapsto (\varphi_v \mapsto$ the $v$-component of $\mathrm{pr}\,\Theta)$ is the nonzero equivariant map $\beta$. $\square$

The main theorem follows: the tools hold by the Proposition, and the height exists because the stabilizer of the doubled lattice is compact. This last step is one application of the lift from the tools.

**Remark 6.6.8 (Formalization).** The proof of the lift from the tools builds the lift map twice, once as an input of the step that reads off the weights and once as a separate input ([TPGTop.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/TPGTop.lean#L46)). The unfolding tool (item 8) is a field of the list, but no proof in the chain reads that field; the one use of the unfolding calls the theorem directly ([ThkBaseKPair.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/ThkBaseKPair.lean#L67)). The decomposition of the adelic group takes the list of tools as a hypothesis and does not use it ([TPGDecomp.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/TPGDecomp.lean#L230)). The non-vanishing theorem raises the heartbeat limit to 2000000 ([TPGNonVan.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/TPGNonVan.lean#L25)). The statement of the main theorem is written three times with the same body: for the good base data of this chapter in [GalTPDefs.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/ThetaKernels/GalTPDefs.lean#L45), again in [HalfIndexLattices/TLiftK.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/HalfIndexLattices/TLiftK.lean#L12), and with the older notion of good base data in [SchurStep.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/SchurStep.lean#L116); a second file with the name TLiftK.lean holds only the second name of the theorem. The definition of a polynomial datum is in a file on divisors ([CTSmallCone.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/CTSmallCone.lean#L39)), and the Weil coefficient is in [ZetaOn.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/ZetaOn.lean#L25). We have not opened the proofs of the Rallis identity, the Schur step, the decomposition, the tail estimate, the coefficient datum, the lift map or the read-off step, so their proofs above give the classical argument and the list of tools that the formal proofs use.
