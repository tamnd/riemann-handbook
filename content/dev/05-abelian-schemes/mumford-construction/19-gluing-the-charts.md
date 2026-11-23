---
title: Gluing the charts
decls:
  - GlobalTheory.Desc.hasExt_of_setup
  - GlobalTheory.Desc.Setup.hasExt
  - GlobalTheory.T.nonempty_descentSeparatedEmbedding
  - GlobalTheory.Desc.nonempty_emb
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Gluing the charts

This section proves the gluing theorem for charts. Let $R$ be a noetherian normal domain, $f \neq 0$ in $R$, and $A$ an abelian scheme over $R[1/f]$ with an ample divisor. Suppose that at every point of $\operatorname{Spec} R$ there is a chart with a semi-abelian group scheme and an ample divisor that matches the divisor of $A$. Then $A$ extends to a semi-abelian scheme over $R$. The proof builds one separated scheme $P$ over $R$ from the sections of the multiples of the divisor. Then $A$ and all the charts embed as open parts of base changes of $P$, and the group law is glued from local pieces. The theorem is Step 6 of [the theorem on extension away from a divisor](/entry/has-ext-away-map-of-charts/). The ample divisors on the charts come from [the theorem on ampleness on a chart](/entry/ample-div-closure-on-chart/).

### The setup

We use charts as defined before [the theorem on extension away from a divisor](/entry/has-ext-away-map-of-charts/), and the notions "induced by" and "restricts to" of [the theorem on ampleness on a chart](/entry/ample-div-closure-on-chart/). For a scheme $Y$ over a ring $S$ and $s \in S$, a *vertical point* of $Y$ for $s$ is a point $z$ with $\dim \mathcal{O}_{Y,z} = 1$ whose image in $\operatorname{Spec} S$ contains $s$.

**Definition 4.19.1 (Gluing setup).** A *gluing setup* consists of the following data.

1. A noetherian, integrally closed domain $R$ and an element $f \neq 0$ of $R$. Write $j : \operatorname{Spec} R[1/f] \to \operatorname{Spec} R$.
2. An abelian scheme $A$ over $R[1/f]$ whose total space is integral, and an ample Cartier divisor $D$ on $A$.
3. For every point $x$ of $\operatorname{Spec} R$, a chart of $(j, A)$ at $x$, with complete regular local ring $R_x$, semi-abelian group scheme $G_x$ with integral total space, and map $\alpha_x$ from the generic fibre of $G_x$ to $A$.
4. A flat ring map $\rho_x : R \to R_x$ such that the chart morphism $\operatorname{Spec} R_x \to \operatorname{Spec} R$ is $\operatorname{Spec} \rho_x$.
5. The open $V_x$ of $G_x$ of points whose image in $\operatorname{Spec} R_x$ does not contain $\rho_x(f)$, and a morphism $\varphi_x : V_x \to A$ that makes the square over $\operatorname{Spec} \rho_x$ and $j$ cartesian and agrees with $\alpha_x$ on the generic fibre.
6. A field map $\theta_x : K(A) \to K(G_x)$ induced by $\varphi_x$.
7. An ample Cartier divisor $D_1(x)$ on $G_x$ that restricts to $\varphi_x^*D$ and has local equation $1$ at every vertical point of $G_x$ for $\rho_x(f)$.

Lean: `GlobalTheory.Desc.Setup`.

Let $c_0 : R \to K(A)$ be the map of constants. Let $W_x$ be the set of $u \in K(A)$ such that $\theta_x(u)$ is regular at every vertical point of $G_x$ for $\rho_x(f)$. For $k \geq 0$ put

$$
N_k = \{\, u \in \Gamma(kD) : u \in W_x \text{ for every } x \,\}.
$$

These are the sections of $kD$ that extend over the vertical divisors of all charts.

**Definition 4.19.2 (Compatible charts).** A gluing setup has *compatible charts* if the following holds. Let $x, x'$ be points of $\operatorname{Spec} R$, $\Omega$ a field, and $u : R_x \to \Omega$, $u' : R_{x'} \to \Omega$ ring maps such that $\ker u'$ is the maximal ideal and $u \circ \rho_x = u' \circ \rho_{x'}$. Then there are:

1. a regular local domain $E$, flat maps $a : R_x \to E$ and $b : R_{x'} \to E$ with $a \circ \rho_x = b \circ \rho_{x'}$, and $v : E \to \Omega$ with kernel $\mathfrak{m}_E$, $v \circ a = u$ and $v \circ b = u'$;
2. the equality $(\ker u) E = \mathfrak{m}_E$;
3. a semi-abelian group scheme $H$ over $E$ with integral total space that is the group pullback of $G_x$ along $\operatorname{Spec} a$ and of $G_{x'}$ along $\operatorname{Spec} b$, by maps whose induced field maps $\theta_a$, $\theta_b$ satisfy $\theta_a \circ \theta_x = \theta_b \circ \theta_{x'}$.

Lean: `GlobalTheory.Desc.Setup.Common`.

**Definition 4.19.3 (Separated model).** A *separated model* of a gluing setup consists of an integral scheme $P$, a separated morphism $p : P \to \operatorname{Spec} R$, a field map $\psi : K(P) \to K(A)$, and the following morphisms.

1. A morphism $\iota_A : A \to P$ that induces $\psi$ and makes the square with sides $\iota_A$, $A \to \operatorname{Spec} R[1/f]$, $p$ and $j$ cartesian.
2. For every $x$ a morphism $e_x : G_x \to P$ over $\operatorname{Spec} \rho_x$ that induces $\theta_x \circ \psi$ and such that the induced map $G_x \to P \times_R \operatorname{Spec} R_x$ is an open immersion.
3. The equality $\iota_A \circ \varphi_x = e_x|_{V_x}$ for every $x$.

Lean: `GlobalTheory.Desc.Emb`.

### The separated model

**Theorem 4.19.4 (Separated model).** Every gluing setup with compatible charts has a separated model.

Lean: `GlobalTheory.Desc.nonempty_emb` (also `GlobalTheory.T.nonempty_descentSeparatedEmbedding`, a second name).

*Proof.* *Step 1: a graded family.* By an input, $1 \in N_0$, each $N_k$ is an $R$-submodule of $K(A)$ through $c_0$, and $N_k N_l \subseteq N_{k+l}$. Also there are $k_0 \geq 1$ and $b_0 \neq 0$ in $N_{k_0}$.

*Step 2: the model $P$.* By an input on graded families, there are an integral scheme $P$, a separated $p : P \to \operatorname{Spec} R$, a field map $\psi : K(P) \to K(A)$ with $\psi \circ c_P = c_0$ for the constants $c_P$ of $P$, and opens $P_{k,b}$ for $k \geq 1$ and $b \in N_k$, with these properties:

1. each $P_{k,b}$ is affine, and the $P_{k,b}$ cover $P$;
2. the generic point is in $P_{k,b}$ if and only if $b \neq 0$;
3. for $b \neq 0$, $\psi$ maps the regular functions on $P_{k,b}$ onto the set of $a / b^m$ with $m \geq 0$ and $a \in N_{km}$;
4. for $z \in P_{k,b}$, $l \geq 1$ and $a \in N_l$, we have $z \in P_{l,a}$ if and only if $a^k / b^l$ is the image of a unit at $z$.

So $P$ is the projective spectrum of $\bigoplus_k N_k$, read through its function field.

*Step 3: constants.* The scheme $A$ is flat over $R[1/f]$ and $R$ is a domain with $f \neq 0$, so $c_0$ is injective.

*Step 4: sections on $A$.* By an input, $\Gamma(kD)$ is the $R[1/f]$-span of $N_k$. Since $D$ is ample, a second input gives that the loci $A_u$ for $u \in N_k$ and $k \geq 1$ cover $A$.

*Step 5: the map $\iota_A$.* By an input, there is a morphism $\iota_A : A \to P$ over $j$ that induces $\psi$ and satisfies $\iota_A^{-1}(P_{k,b}) = A_b$.

*Step 6: open immersion.* The map $R \to R[1/f]$ is flat. Elements of $K(A)$ that are linearly independent over $R$ stay linearly independent over $R[1/f]$. By an input on flat base change, these facts and Step 3 make the induced map $g : A \to P \times_R \operatorname{Spec} R[1/f]$ an open immersion.

*Step 7: the square is cartesian.* The scheme $A$ is proper over $R[1/f]$ and the target of $g$ is separated over $R[1/f]$, so the image of $g$ is closed. It is also open and not empty. The target is an open subscheme of the integral scheme $P$, so it is connected. Hence $g$ is a surjective open immersion, that is, an isomorphism.

*Step 8: the charts.* Fix $x$. By an input, $\Gamma(kD_1(x))$ is the $R_x$-span of $\theta_x(N_k)$, and $\theta_x(N_k) \subseteq \Gamma(kD_1(x))$ because $D_1(x)$ restricts to $\varphi_x^*D$ and elements of $N_k$ lie in $W_x$. As $D_1(x)$ is ample, Steps 4 to 6 apply with $\rho_x$ in place of $R \to R[1/f]$. They give $e_x : G_x \to P$ over $\operatorname{Spec} \rho_x$ that induces $\theta_x \circ \psi$, such that $G_x \to P \times_R \operatorname{Spec} R_x$ is an open immersion.

*Step 9: agreement on $V_x$.* The morphisms $\iota_A \circ \varphi_x$ and $e_x|_{V_x}$ lie over the same map to $\operatorname{Spec} R$, and both induce $\theta_x \circ \psi$, so they agree on the generic point of $V_x$. The generic point is dense in the integral scheme $V_x$ and $P$ is separated over $R$, so the two morphisms are equal. $\square$

### The gluing theorem

For a separated model, let $U \subseteq P$ be the union of the images of the closed fibres of the $G_x$.

**Theorem 4.19.5 (Gluing theorem for charts).** Let a gluing setup be given. Then there are a semi-abelian group scheme $G$ over $\operatorname{Spec} R$ and a morphism $e : A \to G$ that makes $A$ the group pullback of $G$ along $j$.

Lean: `GlobalTheory.Desc.Setup.hasExt` (also `GlobalTheory.Desc.hasExt_of_setup`, a second name).

*Proof.* *Step 1.* By an input, every gluing setup has compatible charts.

*Step 2.* By the theorem on the separated model, there is a separated model $(P, p, \psi, \iota_A, e_x)$.

*Step 3.* By an input, for every point $x$ of $\operatorname{Spec} R$ there are $g \in R$ with $g \notin x$, a group scheme $H$ over $R[1/g]$ and a morphism $h : H \to P$ with these properties. The scheme $H$ is smooth and quasi-compact over $R[1/g]$. The morphism $h$ is an open immersion over $\operatorname{Spec} R$. The products in $H$ and in $A$ agree in $P$. The image of $h$ is $U \cap p^{-1}(D(g))$.

*Step 4.* By an input, these local group schemes give a semi-abelian group scheme $G$ over $R$ and the morphism $e$. $\square$

The model $P$ carries no group law. The local group schemes of Step 3 supply one near each point of $\operatorname{Spec} R$, and their products are those of $A$.

**Remark 4.19.6 (Formalization).** The second names are wrappers ([HasExtOfSetup.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasExtOfSetup.lean#L20)). Steps 1, 3 and 4 of the gluing theorem are `GlobalTheory.T.abelianSchemeDescentData_charts_common`, `GlobalTheory.T.exists_localGroup_range_union_closedFibres` and `GlobalTheory.T.extendsToSemiAbelian_of_local_groups`. Step 1 holds for every setup, so the hypothesis of compatible charts in the theorem on the separated model is always met. That theorem does not use the hypothesis: its proof begins with `intro σ _` ([NonemptyDescentSeparatedEmbedding.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/NonemptyDescentSeparatedEmbedding.lean#L136)). Its Steps 1, 2, 4, 5, 6 and 8 are `GlobalTheory.T.abelianSchemeDescent_gradedFamily_nonzero`, `GlobalTheory.T.exists_integral_separated_projModel_gradedFunctions`, `GlobalTheory.T.cartierMultipleGlobalSections_eq_span_regularLattice` with `GlobalTheory.T.exists_cartierSectionLocus_of_ample_span`, `GlobalTheory.T.exists_map_integral_scheme_to_graded_proj_model`, `GlobalTheory.T.isOpenImmersion_to_graded_model_flat_base_change` with the local lemma `linDisj_A`, and `GlobalTheory.T.cartierMultipleGlobalSections_chart_eq_span`. Steps 7 and 9 are the local lemmas `cartA_of_openIn` and `onV_of`. The properties of $P$ in Step 2 are the fields of `GlobalTheory.Desc.IsModel`, and the gluing setup, its sets $N_k$ and the separated model are in [SubsetSpanBy.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/SubsetSpanBy.lean#L123). A vertical point is `GlobalTheory.Desc.Vert`, with the dimension of the local ring given by `ringKrullDim`. We did not open the proofs of the inputs. The reading of Step 2 as a projective spectrum is ours.
