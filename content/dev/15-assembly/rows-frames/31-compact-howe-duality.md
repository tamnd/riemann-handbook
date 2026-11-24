---
title: Compact Howe duality
decls:
  - GlobalTheory.T.compactHoweDuality_isotypic_mem_of_stable_subspace
  - GlobalTheory.HoweGen.cvType_mem_of_stable
  - GlobalTheory.T.howeDuality_compactPair_realPlaces_irreducible
  - GlobalTheory.HoweIrrCompact.howe_irr
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Compact Howe duality

At the real places, the group $G_\infty$ of Section 30 is compact: it is a product of compact unitary groups, one for each archimedean index $\tau$. The pair formed by $G_\infty$ and the Lie algebra of $U(W)$ acts on the Fock polynomial ring $\mathcal{P}$, and the two actions commute. Howe duality for such a pair says that the isotypic component of an irreducible representation of $G_\infty$ in $\mathcal{P}$ is irreducible under the Lie algebra, after the multiplicity space is accounted for. This section states the two forms of this fact that are used in [the vanishing of equivariant forms](/entry/forms-vanish-of-io/), and reduces them to the algebraic statement of Section 32.

### Equivariant maps

We keep the notation of Section 30: the Fock vectors $\phi_P$ for $P \in \mathcal{P}$, the coefficient space $\mathcal{E}$ with the representation $\rho$, the lowest types $L$ with the map $\iota \colon L \to \operatorname{Hom}(\mathcal{E}, \mathcal{P})$, and the Lie algebra of $U(W)$ at $\tau$ with its one-parameter subgroups $\exp(sY)$.

A linear map $\varphi \colon \mathcal{E} \to \mathcal{P}$ is *equivariant* if
$$\phi_{\varphi(\rho(u) e)} = \omega(u, 1)\, \phi_{\varphi(e)} \qquad \text{for all } u \in G_\infty,\ e \in \mathcal{E}.$$
For linear maps $\psi, \psi' \colon \mathcal{E} \to \mathcal{P}$, say that $\psi'$ is a *derivative* of $\psi$ along $Y$ if, for every $e$ and every point $z$, the function $s \mapsto \omega(1, \exp(sY))\, \phi_{\psi(e)}(z)$ has derivative $\phi_{\psi'(e)}(z)$ at $s = 0$.

**Theorem 7.31.1 (Irreducibility for the compact pair).** Assume the given conditions on $(R, F)$ and that $\omega$ is a full Weil representation. Let $M$ be a space of linear maps $\mathcal{E} \to \mathcal{P}$ such that:

1. every $\psi \in M$ is equivariant;
2. if $\psi \in M$ and $\psi'$ is a derivative of $\psi$ along some $Y$ in the Lie algebra of $U(W)$ at some $\tau$, then $\psi' \in M$;
3. $M \neq 0$.

Then $M$ contains every equivariant linear map $\varphi \colon \mathcal{E} \to \mathcal{P}$.

Lean: `GlobalTheory.T.howeDuality_compactPair_realPlaces_irreducible` (also `GlobalTheory.HoweIrrCompact.howe_irr`).

*Proof.* We translate the hypotheses into the language of the polynomial Fock model and apply the theorem of Section 32.

1. The real points act on Fock vectors through a basis. There are a signature $w$, with an integer $p_\tau$ for each $\tau$, a basis $B$ of the Fock space, and a homomorphism $r$ from $G_\infty$ to the product over $\tau$ of the general linear groups, such that $\omega(u, 1)$ acts on Fock vectors as the Fock action $\mathrm{Fock}(r(u))$, and $r$ maps onto the group of elements that are unitary in the basis $B$ at every $\tau$.
2. The map $P \mapsto \phi_P$ is injective. So a map $\psi$ is equivariant if and only if $\psi(\rho(u) e) = \mathrm{Fock}(r(u))\, \psi(e)$ for all $u$ and $e$.
3. The representation $\mathcal{E}$ of $G_\infty$ is irreducible. The coefficient representation is irreducible under $U(V)(\mathbb{A})$ and trivial on the finite part, and each element of $U(V)(\mathbb{A})$ is the product of its infinite part and its finite part.
4. Let $T_\tau(Z)$ be the operator on $\mathcal{P}$ attached to a complex matrix $Z$ at $\tau$ by the Fock model, with the signs given by $p_\tau$. Then $M$ is stable under $\psi \mapsto T_\tau(Z) \circ \psi$ for every $Z$. For $Y$ in the Lie algebra, the derivative of $\psi$ along $Y$ is $(T_\tau(f Y f^{-1}) + \kappa(Y)) \circ \psi$, where $f$ is the frame at $\tau$ and $\kappa(Y)$ is a scalar. Since $M$ is a subspace that contains $\psi$, it contains $T_\tau(f Y f^{-1}) \circ \psi$. The conjugates $f Y f^{-1}$ span all complex matrices, since the complexification of a unitary Lie algebra is the full matrix algebra. By linearity of $Z \mapsto T_\tau(Z)$ the stability holds for all $Z$.
5. By the theorem on the polynomial Fock model at all real places, a nonzero space of equivariant maps that is stable under all $T_\tau(Z)$ contains every equivariant map.

So $\varphi \in M$. $\square$

### Isotypic membership

**Theorem 7.31.2 (Isotypic membership).** Assume the given conditions on $(R, F)$ and that $\omega$ is a full Weil representation. Let $U \subseteq \mathcal{P}$ be a subspace such that:

1. if $u \in G_\infty$, $P \in U$ and $\phi_{P'} = \omega(u, 1)\phi_P$, then $P' \in U$;
2. if $P \in U$, $Y$ lies in the Lie algebra of $U(W)$ at $\tau$, and $\phi_{P'}(z)$ is the derivative at $s = 0$ of $\omega(1, \exp(sY))\phi_P(z)$ for every $z$, then $P' \in U$;
3. $\iota(x)(e) \in U$ for all $x \in L$ and $e \in \mathcal{E}$.

Then $\varphi(e) \in U$ for every equivariant $\varphi \colon \mathcal{E} \to \mathcal{P}$ and every $e \in \mathcal{E}$.

Lean: `GlobalTheory.T.compactHoweDuality_isotypic_mem_of_stable_subspace` (also `GlobalTheory.HoweGen.cvType_mem_of_stable`).

*Proof.* Let $M$ be the set of equivariant maps $\psi \colon \mathcal{E} \to \mathcal{P}$ with $\psi(e) \in U$ for all $e$.

1. $M$ is a subspace, because the map $P \mapsto \phi_P$ and the operators $\omega(u, 1)$ are linear and $U$ is a subspace.
2. For each $x \in L$, the map $\iota(x)$ lies in $M$. It is equivariant by the laws of the theta vector, and its values lie in $U$ by property 3.
3. $M \neq 0$. The laws of the theta vector give a pure tensor $x \in L$ and a vector $e$ with $\iota(x)(e)$ equal to a nonzero vector of the lowest type. So $\iota(x) \neq 0$, and $\iota(x) \in M$ by step 2.
4. $M$ satisfies the hypotheses of the theorem above. Each element is equivariant by definition. If $\psi \in M$ and $\psi'$ is a derivative of $\psi$ along $Y$, then $\psi'$ is equivariant, since the action of the Lie algebra of $U(W)$ commutes with the action of $G_\infty \subseteq U(V)$. Its values lie in $U$ by property 2, applied to each $\psi(e)$.

By the theorem above, $\varphi \in M$, so $\varphi(e) \in U$. $\square$

The space $U$ in the application is the common kernel of a family of equivariant forms. The theorem says that this kernel contains the full isotypic component of type $\mathcal{E}$ once it contains the image of the lowest types. In the classical language, the lowest types generate the isotypic component as a module over the Lie algebra of $U(W)$, which is a consequence of the irreducibility in Howe duality.

**Remark 7.31.3 (Formalization).** The relay for irreducibility is at line 18 of [HoweDualityCompactPairRealPlacesIrreducibleStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/HoweDualityCompactPairRealPlacesIrreducibleStatement.lean#L18), and its target `howe_irr` is at line 46 of [HoweDualityCompactPairRealPlacesIrreducible.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/HoweDualityCompactPairRealPlacesIrreducible.lean#L46). Step 1 is `realPoints_act_fock_by_realComponents_basis`, step 4 uses `hasDerivAt_fockVectors_targetLie_realPlace` for the scalar $\kappa$ and `span_conj_unitaryLieAlgebra_realPlace_eq_top` for the span, and step 5 is `howeDuality_compactPair_polynomialFock_allRealPlaces`. The helpers `fockT_zero`, `fockT_add` and `fockT_smul` at lines 33 to 40 give the linearity of $T_\tau$. The relay for isotypic membership is at line 18 of [CompactHoweDualityIsotypicMemOfStableSubspaceStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CompactHoweDualityIsotypicMemOfStableSubspaceStatement.lean#L18), and its target `cvType_mem_of_stable` is at line 22 of [CompactHoweDualityIsotypicMemOfStableSubspace.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CompactHoweDualityIsotypicMemOfStableSubspace.lean#L22). The equivariance of derivatives in step 4 of its proof is the lemma `fockPolynomial_lieDerivative_equivariant`, and the nonvanishing in step 3 uses `IoExtPf.Delta_ne`. The reason given in step 4, that the two actions commute, is the classical argument; the Lean proof cites the lemma.
