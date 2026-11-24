---
title: The global Weil datum
decls:
  - GlobalTheory.WeilProduct.exists_weilDatum_etaTilde
  - GlobalTheory.T.exists_weilDatum_powers_unramifiedEtaTilde
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The global Weil datum

This section proves that for two Hermitian spaces $S$ and $T$ over a CM field with self-dual lattices, and for a Hecke character $\eta$ of type $\tilde\eta$, there is an adelic Weil representation of $\mathrm{U}(S) \times \mathrm{U}(T)$ on theta functions with splitting characters $\eta^{\operatorname{rank} T}$ and $\eta^{\operatorname{rank} S}$ that has all the properties of a Weil datum, fixes the lattice vacuum at the nonsplit finite places, and acts on the Fock vacuum at infinity by the explicit determinant character. It is the existence statement that the step [every character of the literature](/step/every-character-of-literature/) uses to obtain a Weil representation with known local behaviour. The construction is the product of a finite part and an infinite part, and the [corollary on the theta distribution](/entry/of-oi-apply-zero/) of the previous section gives its automorphy.

We keep the notation of the previous section: the space $\mathbb{W} = M_{b \times a}(\mathbb{A}_E)$, the Heisenberg operators $\rho(w_0)$, the action $(g, h) \cdot x = h x g^{-1}$, theta functions, finite and infinite Weil parts, Cartan involutions and the type $\tilde\eta$.

### Weil data

A *place idempotent* for a finite place $v$ of $F$ is the adele $\varepsilon_v$ with component $1$ at $v$ and $0$ elsewhere. A *split idempotent* is an idempotent $e \in \mathbb{A}_E$ with $e\bar e = 0$ and $e + \bar e = \varepsilon_v$ for a place idempotent $\varepsilon_v$: it picks one of the two places of $E$ above a split place $v$. A place $v$ is *nonsplit* if there is no split idempotent with $e + \bar e = \varepsilon_v$.

**Definition 1.16.1 (Weil datum).** Let $\psi$ be a standard character of sign $-1$ and $\chi_S, \chi_T$ characters of $\mathbb{A}_E^\times$. A representation $\omega$ of $\mathrm{U}(S)(\mathbb{A}_F) \times \mathrm{U}(T)(\mathbb{A}_F)$ on functions on $\mathbb{W}$ is a *Weil datum* for $(\psi, \chi_S, \chi_T)$ if $\chi_S$ and $\chi_T$ are Hecke characters whose restrictions to $\mathbb{A}_F^\times$ are $\eta_{E/F}^{\,a}$ and $\eta_{E/F}^{\,b}$, and:

1. $\omega$ preserves theta functions;
2. $\omega(g, h)\,\rho(w_0) f = \rho((g, h)\cdot w_0)\, \omega(g, h) f$ for all $(g, h)$, all $w_0$ and all theta functions $f$;
3. $(\omega(\gamma, \gamma') f)(0) = f(0)$ for rational $\gamma, \gamma'$ and theta functions $f$;
4. $(g, h) \mapsto (\omega(g, h) f)(w)$ is continuous for each theta function $f$ and each $w$;
5. $\omega$ preserves the $L^2$ norm over a fundamental domain of the rational lattice, for each Haar measure;
6. at a split idempotent $e$, if $g$ and $h$ are supported at $e$ with determinants $x$ and $y$, there is $r > 0$ such that each linear form $\ell$ that is invariant under $\rho(u)$ for $u$ supported at $e$ satisfies
$$\ell(\omega(g, h) f) = r\, \chi_T(x)^{-1} \chi_S(y)\, \ell(f).$$

Condition 2 is the defining property of a Weil representation: it normalizes the Heisenberg group through the action of the unitary groups on $\mathbb{W}$. Condition 3 is Weil's automorphy. Condition 6 fixes the splitting at the split places: there the unitary groups are general linear groups, and the Weil representation is the action on a Schrödinger model twisted by the characters.

**Definition 1.16.2 (Vacuum conditions).** Let $\Lambda_S$, $\Lambda_T$ be lattices and $v$ a nonsplit finite place with place idempotent $\varepsilon$. The representation $\omega$ *fixes the vacuum at $v$* if for $g, h$ supported at $\varepsilon$ such that $(g, h)$ preserves the tensor lattice $\Lambda_v$ of $\Lambda_S$ and $\Lambda_T$ at $v$, and each theta function $f$ fixed by $\rho(u)$ for all $u \in \Lambda_v$, one has $\omega(g, h) f = f$. It *has the vacuum character* for $\theta$ if it acts on Fock vacua at infinity by the product of the determinants of the previous section.

### The theorem

**Theorem 1.16.3 (The global Weil datum).** Let $F$ be totally real, $E/F$ a CM extension, $\psi$ a standard character of sign $-1$, $S$ and $T$ Hermitian spaces of ranks $a$ and $b$, $\theta$ a family of embeddings over the infinite places, $\Lambda_S$ and $\Lambda_T$ self-dual lattices, and $\eta$ a Hecke character of type $\tilde\eta$. Then there is a representation $\omega$ of $\mathrm{U}(S)(\mathbb{A}_F) \times \mathrm{U}(T)(\mathbb{A}_F)$ on functions on $\mathbb{W}$ such that:

1. $\omega$ is a Weil datum for $(\psi, \eta^{a}, \eta^{b})$;
2. $\omega$ fixes the vacuum at each nonsplit finite place;
3. $\omega$ has the vacuum character for $\theta$.

Lean: `GlobalTheory.WeilProduct.exists_weilDatum_etaTilde` (also `GlobalTheory.T.exists_weilDatum_powers_unramifiedEtaTilde`, a second name).

*Proof.* The characters $\eta^a$ and $\eta^b$ are Hecke characters, and their restrictions to $\mathbb{A}_F^\times$ are $\eta_{E/F}^{\,a}$ and $\eta_{E/F}^{\,b}$, since $\eta$ restricts to $\eta_{E/F}$. By the existence of the finite part, there is a finite Weil part $\omega_{\mathrm f}$ for $(\eta^a, \eta^b)$ and the lattices, and there is an infinite Weil part $\omega_\infty$ for $\theta$. The two parts commute on theta functions. So
$$p \mapsto \omega_{\mathrm f}(p)\,\omega_\infty(p)$$
is a representation of $\mathrm{U}(S)(\mathbb{A}_F) \times \mathrm{U}(T)(\mathbb{A}_F)$ on the space of theta functions: for $p, q$ one has $\omega_{\mathrm f}(pq)\omega_\infty(pq) = \omega_{\mathrm f}(p)\omega_\infty(p)\omega_{\mathrm f}(q)\omega_\infty(q)$ because $\omega_\infty(p)$ and $\omega_{\mathrm f}(q)$ commute. Extend it to all functions on $\mathbb{W}$ by the identity on a complement of the space of theta functions. Call the result $\omega$. On theta functions, $\omega = \omega_{\mathrm f}$ on the finite subgroup and $\omega = \omega_\infty$ on the archimedean subgroup, since each part is trivial on the other subgroup.

Now check the conditions. Preservation of theta functions holds since both parts preserve them. For the Heisenberg law, write $(g, h) = (g_\infty, h_\infty)(g_{\mathrm f}, h_{\mathrm f})$ as a product of an archimedean and a finite element. The finite part satisfies the Heisenberg law for $(g_{\mathrm f}, h_{\mathrm f})$ and the infinite part for $(g_\infty, h_\infty)$, and $\rho(w_0)$ preserves theta functions, so the law holds for the product, since the action on $\mathbb{W}$ is multiplicative. For automorphy write $(\gamma, \gamma') = (\gamma, 1)(1, \gamma')$. The value at $0$ is invariant under $(\gamma, 1)$ by the source case of the invariance and under $(1, \gamma')$ by the [corollary](/entry/automorphy-target/) of the previous section. Continuity follows from the continuity of the product of the two parts. Unitarity follows since each part is unitary. At a split idempotent, elements supported at $e$ lie in the finite subgroup, so $\omega = \omega_{\mathrm f}$ there and the split law is that of the finite part. In the same way, elements supported at a nonsplit finite place lie in the finite subgroup, and the vacuum condition is that of the finite part. Archimedean elements act by $\omega_\infty$, which has the vacuum character. $\square$

**Remark 1.16.4.** The theorem is a form of the existence of the global Weil representation of a unitary dual pair with prescribed splitting characters, due to A. Weil, *Sur certains groupes d'opérateurs unitaires*, Acta Math. 111 (1964), Chapter I, for the metaplectic group, with the splitting over unitary groups of S. Kudla, *Splitting metaplectic covers of dual reductive pairs*, Israel J. Math. 87 (1994), Section 3, and M. Harris, S. Kudla and W. J. Sweet, *Theta dichotomy for unitary groups*, J. Amer. Math. Soc. 9 (1996), Section 1. The model here is the space of theta functions on $\mathbb{W}$, which is the image of the Schrödinger model under the theta distribution, and the splitting characters are the powers $\eta^a, \eta^b$ of one unramified character of type $\tilde\eta$, so that the local splittings are unramified at every finite place.

**Remark 1.16.5 (Formalization).** The theorem is `exists_weilDatum_etaTilde` ([ExistsWeilDatumPowersUnramifiedEtaTilde.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsWeilDatumPowersUnramifiedEtaTilde.lean#L48)), and its second name is a wrapper under `maxHeartbeats`. The two parts come from `exists_isFinWeil` (ExistsIsFinWeil.lean, line 251) and `GlobalTheory.RealWeil.exists_isInfWeil` (LintegralEqOfNorms.lean, line 261), and they commute by `fin_inf_comm` (ContinuousProduct.lean, line 66). The extension to all functions is `exists_extend` (LintegralEqOfNorms.lean, line 143): it uses an arbitrary complement of the theta functions, chosen by choice, and acts by the identity on it. So the representation is only determined on theta functions, and all conditions of a Weil datum are stated for theta functions only. The automorphy for $(\gamma, 1)$ is the cited result `thetaDistribution_automorphy_source_group`, which this chapter cites and does not prove; the case $(1, \gamma')$ is `thetaDistribution_invariant_rationalTarget`. The restriction condition of a Weil datum says that a character with the defining property of $\eta_{E/F}$ exists and that the restriction is a power of every such character.
