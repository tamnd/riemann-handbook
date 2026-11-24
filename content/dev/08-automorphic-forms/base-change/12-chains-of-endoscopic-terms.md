---
title: Chains of endoscopic terms
decls:
  - PositivityTheory.Rg.BcB.F.F0.chain_existence_of_global_character
  - PositivityTheory.Rg.BcB.F.F0.chainEx_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Chains of endoscopic terms

The elliptic part of the trace formula of the unitary group $U(n)$ is a sum over elliptic characteristic polynomials of $\kappa$-orbital integrals. This section writes it, for test functions that match at a section, as a finite linear combination of the elliptic parts of the twisted trace formulas of the groups $\mathrm{GL}_a \times \mathrm{GL}_{n-a}$ over $E$, with explicit archimedean weights. A family of such data, one term for each endoscopic group $U(a) \times U(n-a)$ that occurs, is a chain. The chain is part of the frame of [Section 7.16.2](/entry/frame-ex0/), where it turns the unitary spectral side into twisted spectral sides of general linear groups. The proof combines three results: the stabilization of the unitary elliptic sum, taken as given, [the theorem on elliptic terms](/entry/global-character-of-finite-inputs/) of Section 07, and [the stable elliptic sum](/entry/g3/) of Section 11.

We keep the notation of Sections 04, 07 and 11. Let $E$ be a CM field with maximal real subfield $F$, in which every finite place is unramified over $F$, and let $r_E$ be the number of archimedean places of $E$. For a dominant weight $l = (l_1 \ge \dots \ge l_m)$ of $\mathrm{GL}_m$ let
$$\chi(l) = \{l_k + \tfrac{m-1}{2} - (k - 1) : 1 \le k \le m\},$$
a multiset of $m$ complex numbers. This is the infinitesimal character of the irreducible representation of highest weight $l$, written as the multiset of its Harish-Chandra parameters. For a multiset $X$ and $s \in \mathbb{C}$ let $X + s$ be the multiset of the $x + s$.

**Definition 7.12.1 (Admissible character).** Let $\mu$ be a unitary Hecke character of $E$ and $e = (e_v)$ a family of integers indexed by the archimedean places. The pair $(\mu, e)$ is admissible if:

1. the restriction of $\mu$ to the ideles of $F$ is the quadratic character of $E/F$;
2. at every inert finite place $w$, $\mu_w$ is the unramified character with value $-1$ at a uniformizer;
3. every $e_v$ is odd;
4. the archimedean component of $\mu$ is $z \mapsto \prod_v(z_v/|z_v|)^{e_v}$.

Such a $\mu$ defines the base change of a representation of $U(a) \times U(n-a)$ to $\mathrm{GL}_a \times \mathrm{GL}_{n-a}$: the twist by $\mu^{n-a}$ on the first factor and by $\mu^a$ on the second makes the parameters of the two factors fit together, and $e_v$ records the archimedean shift.

**Definition 7.12.2 (Unitary elliptic sum).** Let $S$ be a section, $\lambda = (\lambda_v)$ a family of dominant weights of $\mathrm{GL}_n$, and $f = (f_w)$ a family of functions on the groups $U_w$. Put
$$\mathcal{G}_U(S, \lambda, f) = \sum_{a = 0}^n\sum_{(P_1, P_2)}\mathfrak{m}(P_1P_2)\,\mathrm{ch}_\lambda(P_1P_2)\prod_{w \in S}\kappa O_{P_1,P_2}(f_w),$$
the inner sum over the coprime pairs of elliptic polynomials of degrees $a$ and $n - a$.

This is the elliptic part of the trace formula of $U(n)$, sorted by the endoscopic data $(P_1, P_2)$: for each elliptic $P = P_1P_2$, the $\kappa$-orbital integral picks out the part attached to $U(a) \times U(n-a)$.

**Definition 7.12.3 (Chain).** Let $n \ge 1$, $(\mu, e)$ admissible and $\lambda$ a family of dominant weights of $\mathrm{GL}_n$. A chain for $(\mu, e, \lambda)$ consists of:

1. a finite nonempty set $I$, and for each $i \in I$ an integer $0 \le a_i \le n$ and families $l_{1,i}$, $l_{2,i}$ of dominant weights of $\mathrm{GL}_{a_i}$ and $\mathrm{GL}_{n-a_i}$, such that for every archimedean $v$
$$\big(\chi(l_{1,i,v}) + \tfrac{(n - a_i)e_v}{2}\big) + \big(\chi(l_{2,i,v}) + \tfrac{a_ie_v}{2}\big) = \chi(\lambda_v)$$
as multisets;
2. Haar measures on all $\mathrm{GL}_m(\mathbb{A}_E)$ and $\mathrm{GL}_m(\mathbb{C})$;
3. coefficients $c_i \in \mathbb{C}$;

such that the following identity holds. Let $S$ be a section, $K'$ a level family of $U(n)$ and $f$ a test function of level $K'$. For every $a$ let $u_{1,a}$ and $u_{2,a}$ be translators of $\mathrm{GL}_a$ and $\mathrm{GL}_{n-a}$, and let $\varphi^1_a$, $\varphi^2_a$ be families on $\mathrm{GL}_a(E_w) \times \mathrm{GL}_{n-a}(E_w)$, such that for every $a \le n$ the families $\varphi^1_a$, $\varphi^2_a$ and $s_a$ (formed from them as in Section 07) are local test families and $f_w$ matches $s_{a,w}$ with the character $\mu_w$ at every $w \in S$. Assume that for every $i$ there is $w \in S$ at which $s_{a_i,w}$ vanishes off the pairs whose norm polynomials have a separable product. Let $\psi_{i,v}$ be a Lefschetz function for $(l_{1,i,v}, l_{2,i,v})$ with value $c_{i,v}$, and let $z \in \mathbb{C}$ with $\prod_vc_{i,v} = z$ for every $i$. Let $\Phi_i$ be the function built from $\psi_{i,\cdot}$, $u_{1,a_i}$, $u_{2,a_i}$, $\varphi^1_{a_i}$ and $\varphi^2_{a_i}$ as in the theorem on elliptic terms. Then
$$z\,\mathcal{G}_U(S, \lambda, f) = \sum_{i \in I}c_i\sum_{\mathrm{ell}}O(\Phi_i).$$

The identity says that a unitary elliptic sum, multiplied by a common archimedean value $z$, is a combination of twisted elliptic sums of the groups $\mathrm{GL}_{a_i} \times \mathrm{GL}_{n - a_i}$. The condition on $\chi$ says that the archimedean parameters of the endoscopic terms fit together to the parameter $\chi(\lambda_v)$ of $U(n)$.

We take the stabilization from the companion development.

**Theorem 7.12.4 (Stabilization of the unitary elliptic sum).** Let $n \ge 1$, $(\mu, e)$ admissible and $\lambda$ a family of dominant weights. There are a finite set $I$, integers $a_i \le n$, families of dominant weights $l_{1,i}$, $l_{2,i}$ satisfying the condition of part 1 of the definition of a chain, and nonzero $\sigma_i \in \mathbb{C}$ with the following property. Let $S$ be a section, $K'$ a level family, $f$ a test function of level $K'$, and for every $a \le n$ let $\varphi_a$ be a local test family that matches $f$ with $\mu$ at every $w \in S$. Then
$$\mathcal{G}_U(S, \lambda, f) = \sum_{i \in I}\sigma_i\,\mathcal{G}_{\mathrm{st}}(S, l_{1,i}, l_{2,i}, \varphi_{a_i}).$$

Lean: `PositivityTheory.Rg.BcB.F.F0.complex_coefficient_multiplicity_holds`.

*Proof.* This is taken from the companion development, where it is derived from a local identity of elliptic orbital integrals, a statement that the local signs are 1 almost everywhere, and a map from characters to weights. $\square$

**Theorem 7.12.5 (Existence of chains).** Let $E$ be a CM field in which every finite place is unramified over $F$, let $n \ge 1$, $(\mu, e)$ admissible and $\lambda$ a family of dominant weights of $\mathrm{GL}_n$. Then there is a chain for $(\mu, e, \lambda)$.

Lean: `PositivityTheory.Rg.BcB.F.F0.chainEx_holds` (also `PositivityTheory.Rg.BcB.F.F0.chain_existence_of_global_character`, the same result with the theorem on elliptic terms as a hypothesis).

*Proof.* Take $I$, $a_i$, $l_{1,i}$, $l_{2,i}$ and $\sigma_i$ from the stabilization of the unitary elliptic sum, and choose Haar measures on all $\mathrm{GL}_m(\mathbb{A}_E)$ and $\mathrm{GL}_m(\mathbb{C})$. For each pair $(a, b)$, the [theorem on elliptic terms](/entry/global-character-of-finite-inputs/) gives a constant $c_{a,b} \ne 0$ for these measures. Let $I' = I \sqcup \{\ast\}$. For $i \in I$ keep the data and put
$$c_i = \frac{\sigma_i}{c_{a_i,n-a_i}\,2^{nr_E}}.$$
For the extra index put $a_\ast = n$, $l_{1,\ast} = \lambda$, $l_{2,\ast}$ the empty weight of $\mathrm{GL}_0$, and $c_\ast = 0$. Then $\chi$ of the empty weight is the empty multiset, so the condition on $\chi$ holds for $\ast$, and $I'$ is not empty.

Now take $S$, $f$, the translators, the families $\varphi^1_a$, $\varphi^2_a$, the Lefschetz functions and $z$ as in the definition. The term of $\ast$ is 0. Fix $i \in I$ and write $a = a_i$, $b = n - a$. By the theorem on elliptic terms,
$$\sum_{\mathrm{ell}}O(\Phi_i) = c_{a,b}\prod_vc_{i,v}\,\mathcal{G}_{\mathrm{rat}}(S, l_{1,i}, l_{2,i}, s_a) = c_{a,b}\,z\,\mathcal{G}_{\mathrm{rat}}(S, l_{1,i}, l_{2,i}, s_a).$$
Since $s_a$ is a local test family and satisfies the regularity condition at some $w \in S$, the [stable elliptic sum](/entry/g3/) gives $\mathcal{G}_{\mathrm{rat}} = 2^{(a+b)r_E}\mathcal{G}_{\mathrm{st}} = 2^{nr_E}\mathcal{G}_{\mathrm{st}}$. Hence
$$c_i\sum_{\mathrm{ell}}O(\Phi_i) = z\,\sigma_i\,\mathcal{G}_{\mathrm{st}}(S, l_{1,i}, l_{2,i}, s_{a_i}).$$
Summing over $i$ and applying the stabilization to the families $s_a$, which match $f$ with $\mu$ on $S$, gives $z\,\mathcal{G}_U(S, \lambda, f)$. For the unconditional form, the theorem on elliptic terms is proved in Section 07 by [its final form](/entry/global-character-holds/). $\square$

**Remark 7.12.6 (Formalization).** A chain is the structure `PositivityTheory.Rg.BcB.F.Chain` (SatakeExponents/UniformizerValuations/FrameA.lean:23), and the statement is `ChainEx` (same file, line 109). The proof is `chainEx_of` (HyperbolicEntryBounds/InfinitesimalWeightZero.lean:42). It pads the index set with `none`, with coefficient 0 and $a = n$, only to make the index type nonempty, as the structure requires (lines 51 to 64); the padded term contributes nothing. The stabilization is `G8.GlobalComplexCoefficients` (ThetaNormCommutation/GlobalComplexCoefficients.lean:12), proved in ChainPlug.lean by `GlobalTheory.T.globalComplexCoefficients_of_local_orbit_character` from three inputs, which we did not open. The unitary elliptic sum is `geomU` (SimpleTwistedTraceFormulaStable.lean:235), with the stable mass of the product $P_1P_2$; the infinitesimal character is `infOfWeight` (BaseChangeDefiniteUnitary.lean:142); admissibility is `IsMu` (IsUnifAt.lean:46). The constant in the chain identity multiplies the unitary side, and the Lefschetz values must have the same product $z$ for all $i$; the chain does not record which $z$ occurs. The name `chain_existence_of_global_character` refers to the input `G8.G4`, the theorem on elliptic terms, not to a global character.
