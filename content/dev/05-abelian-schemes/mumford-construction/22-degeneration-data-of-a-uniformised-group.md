---
title: Degeneration data of a semi-abelian scheme
decls:
  - GlobalTheory.T.exists_degenerationData_uniformisation_of_torsionCount
  - GlobalTheory.UU.exists_degData_unif
  - GlobalTheory.T.exists_uniformisation_data_before_choice
  - GlobalTheory.PreUnif.exists_preU
  - GlobalTheory.T.exists_degenerationData_functionalEquation_degree_one
  - GlobalTheory.UU.exists_degData_fe_one
  - GlobalTheory.UU.unif_assembly
  - GlobalTheory.T.exists_uniformisation_of_functionalEquation_degreeOne
  - GlobalTheory.UU.exists_unif_of_fe_one
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Degeneration data of a semi-abelian scheme

This section proves the converse of Mumford's construction over a complete discrete valuation ring. A semi-abelian scheme whose generic fibre is a polarised abelian variety, with a cubical line bundle and a split torus on the closed fibre, has degeneration data, and the data uniformise it. The proof has three parts. First it builds the data without the conditions on $\psi$, from the tower of thickenings of the closed fibre. Then it chooses $\psi$ again so that the theta expansions satisfy the functional equation in degree one. Last it shows that this one functional equation gives a full uniformisation. The result is used in [the step on every character](/step/every-character/). For the classical construction see [semi-abelian degenerations and Mumford's construction](/learn/abelian-varieties/#semi-abelian-degenerations-and-mumfords-construction) in Volume 1.

### The classical statement

Let $S$ be a noetherian normal scheme complete along a closed subscheme, and $G$ a semi-abelian scheme over $S$ whose generic fibre is an abelian variety with an ample line bundle, and whose torus part over the closed subscheme is split. Faltings and Chai attach degeneration data to $G$ and show that Mumford's construction applied to these data gives back $G$ (Faltings and Chai, *Degeneration of Abelian Varieties*, Springer 1990, Chapter II). The theorem of this section is this result in the case of a complete discrete valuation ring of characteristic $0$. It assumes two standard inputs as hypotheses, and it keeps the given cubical line bundle on $G$.

### Hypotheses

**Torsion count.** For every algebraically closed field $k$, every abelian variety $B$ over $k$ of dimension $g$ and every integer $n$ that is not zero in $k$, the group $B$ has exactly $n^{2g}$ points $x$ with $nx = 0$. This is a theorem of the classical theory (Mumford, *Abelian Varieties*, Oxford University Press 1970, §4, Application 2). In the theorems below it is a hypothesis.

**Definition 4.22.1 (Laws of abelian schemes).** The *laws of abelian schemes* are a list of twenty-four standard statements on abelian schemes and semi-abelian schemes. Among them are the theorem of the cube, rigidity, the Weil pairing and its nondegeneracy, base change of global sections, the extension of cubical structures, and the equality $\Gamma(B, \mathcal{O}_B) = \Gamma(S, \mathcal{O}_S)$ for an abelian scheme $B$ over $S$. The *second laws* are four more statements: base change of sections over any base, twists of sections, the characters of the Weil pairing, and the density of smooth points.

Lean: `ReciprocityTheory.ChartRestriction.G.Out.Laws` (also `ReciprocityTheory.ChartRestriction.G.Out.Laws2`, the second laws).

The laws are proved elsewhere without hypotheses, so they are hypotheses here only for the structure of the proof.

### Settings and pre-uniformisations

A *complete discrete valuation ring* here is a discrete valuation ring $V$ of characteristic $0$ that is complete for its maximal ideal $\mathfrak{m}$. We write $K = \operatorname{Frac} V$, $\bar K$ for an algebraic closure of $K$, and $G_e = G \otimes_V V/\mathfrak{m}^{e+1}$. A *cubical bundle* on a commutative group scheme is a line bundle rigidified along the zero section, with a cubical structure and a compatible symmetric structure.

**Definition 4.22.2 (Degeneration setting).** Let $V$ be a local domain, $A$ a polarised abelian variety over $K$ with bundle $L_A$, and $G$ a commutative group scheme over $V$. A *degeneration setting* for $(A, G)$ consists of:

1. the fact that $V$ is a complete discrete valuation ring of characteristic $0$;
2. the fact that $G$ is semi-abelian, and an isomorphism of group schemes $G_K \cong A$;
3. a cubical bundle $P$ on $G$ and an isomorphism of $L_A$ with $P|_{G_K}$;
4. a free abelian group $\mathsf{X}$ of finite rank, and on the closed fibre $G_0$ the structure of an extension of an abelian scheme by the split torus with character group $\mathsf{X}$;
5. a cubical bundle $P_0$ on $G_0$ that is the restriction of $P$, and an even cubical trivialisation of $P_0$ on the torus.

Lean: `GlobalTheory.UU.HidaSetting`.

**Definition 4.22.3 (Pre-data).** *Pre-data* over $V$ consist of a polarised abelian scheme $B$ over $V$ with a cubical bundle $L$, a free abelian group $\mathsf{X}$ of finite rank, a homomorphism $c : \mathsf{X} \to B(V)$, and for each $\chi$ a trivialisation $\psi(\chi)$ of $c(\chi)^*L^{-1}$ over $K$. Degeneration data are pre-data such that $\psi$ is even, $\tau$ is bimultiplicative, $\psi(\chi)$ has values in $\mathfrak{m}$ for $\chi \neq 0$, and for each $n$ the value $\psi(\chi)$ lies in $\mathfrak{m}^n$ for all but finitely many $\chi$.

Lean: `ReciprocityTheory.ChartRestriction.G.Out.DegPre` (also `ReciprocityTheory.ChartRestriction.G.Out.DegData`, the degeneration data).

**Definition 4.22.4 (Pre-uniformisation).** Let $D$ be pre-data over $V$. A *pre-uniformisation* of $(A, G)$ by $D$ consists of: the fact that $G$ is semi-abelian; an isomorphism of group schemes $G_K \cong A$; a cubical bundle $P$ on $G$ with an isomorphism $L_A \cong P|_{G_K}$; for each $e$, torus coordinates on $G_e$ and a projection $p_e : G_e \to B$, compatible as $e$ grows; and for each $e$ an isomorphism $P|_{G_e} \cong p_e^*L$ that respects the rigidifications, the cubical and the symmetric structures and is compatible as $e$ grows.

Lean: `GlobalTheory.UU.PreU`.

A uniformisation as in [the first section](/entry/has-of-base/) has the same data. In addition, $G$ is smooth and separated, and for every $k \geq 1$ the theta expansion is a bijection from sections of $L_A^k$ to theta families of level $k$.

**Definition 4.22.5 (Functional equation in degree $k$).** Let $U$ be a pre-uniformisation by pre-data $D$, $F$ a field over $K$ and $k \geq 1$. We say that $U$ *satisfies the functional equation in degree $k$ over $F$* if for every section $t$ of $L_A^k$ over $F$, every family $(s_\chi)$ of theta expansion coefficients of $t$ satisfies

$$
s_{\chi + k\mu} = \psi(\mu)^k \, \tau(\mu, \chi) \, T_{c(\mu)}^* s_\chi \qquad (\chi, \mu \in \mathsf{X}).
$$

Lean: `GlobalTheory.UU.PreU.FE`.

A pre-uniformisation $U$ and a uniformisation $U'$ *match* if they have the same isomorphism $G_K \cong A$, the same cubical bundle, the same torus coordinates and the same isomorphisms $P|_{G_e} \cong p_e^*L$.

### The three steps

**Theorem 4.22.6 (Pre-data from a setting).** Assume the torsion count and the laws of abelian schemes. Let $s$ be a degeneration setting for $(A, G)$ over $V$. Then there are pre-data $D$ over $V$ and a pre-uniformisation $U$ of $(A, G)$ by $D$ with the same cubical bundle $P$ and the same isomorphism $G_K \cong A$ as $s$.

Lean: `GlobalTheory.PreUnif.exists_preU` (also `GlobalTheory.T.exists_uniformisation_data_before_choice`, a second name).

*Proof.* *Step 1: the tower.* By an input, the setting gives a tower of torus quotients. For each $e$, $G_e$ is an extension of an abelian scheme $B_e$ over $V/\mathfrak{m}^{e+1}$ by the split torus of $\mathsf{X}$. The bundle $P|_{G_e}$ descends to a cubical bundle on $B_e$, and the $B_e$ form a compatible system of cubical pullbacks.

*Step 2: algebraisation.* By an input that uses the torsion count and the laws, the system $(B_e)$ algebraises. There are an abelian scheme $B$ over $V$, a cubical bundle $L$ on $B$ that is relatively ample, and maps $B_e \to B$ that identify $B_e$ with $B \otimes V/\mathfrak{m}^{e+1}$ as cubical pullbacks. By a second input, $L$ has the remaining property of a polarisation, so $B$ with $L$ is a polarised abelian scheme.

*Step 3: the periods.* By a lemma, there is a homomorphism $c : \mathsf{X} \to B(V)$ such that for every $e$ the translate of $L$ by $c(\chi)$ is represented on $G_e$ by sections of weight $\chi$ for the torus. For every $\chi$, a trivialisation $\psi(\chi)$ of $c(\chi)^*L^{-1}$ over $K$ exists because $V$ is local. This gives pre-data $D$.

*Step 4: coordinates.* For each $e$, a lemma gives torus coordinates on $G_e$ and the projection $p_e : G_e \to B$, compatible as $e$ grows.

*Step 5: the isomorphisms.* By a lemma, there are isomorphisms $P|_{G_e} \cong p_e^*L$ that respect the structures and are compatible as $e$ grows. They are unique up to an even cubical unit, and such a unit is $1$ by the law $\Gamma(B, \mathcal{O}_B) = \Gamma(V, \mathcal{O}_V)$. This uniqueness gives the compatibility. $\square$

**Theorem 4.22.7 (Functional equation in degree one).** Assume the laws and the second laws. Let $V$ be a complete discrete valuation ring of characteristic $0$, $D$ pre-data over $V$, and $U$ a pre-uniformisation of $(A, G)$ by $D$. Then there are degeneration data $D'$ over $V$ and a pre-uniformisation $U'$ of $(A, G)$ by the pre-data of $D'$ with the same cubical bundle and the same isomorphism $G_K \cong A$ as $U$, such that $U'$ satisfies the functional equation in degree $1$ over $\bar K$.

Lean: `GlobalTheory.UU.exists_degData_fe_one` (also `GlobalTheory.T.exists_degenerationData_functionalEquation_degree_one`, a second name).

*Proof.* *Step 1: a theta section.* By an input, there are a section $\theta$ of $L_A$ and an integral family $f = (f_\chi)$ that is its expansion. By a second input, $f_\chi \neq 0$ for every $\chi$.

*Step 2: a new $\psi$.* By an input, there is a new choice $\psi'$ of trivialisations that is related to the coefficients $f_\chi$ by the theta relation of degree one. Replace $\psi$ by $\psi'$ in $D$. By a lemma, $U$ gives a pre-uniformisation $U'$ by the new pre-data, with the same bundle and isomorphism, and $\theta$ gives a section $\theta'$ with expansion $f$ for $U'$.

*Step 3: the conditions on $\psi'$.* By inputs that use the theta relation, $\psi'$ is even, the new $\tau'$ is bimultiplicative, and for each $n$ only finitely many $\psi'(\chi)$ lie outside $\mathfrak{m}^n$. A lemma derives $\psi'(\chi) \in \mathfrak{m}$ for $\chi \neq 0$ from these three facts. So the new pre-data are degeneration data $D'$.

*Step 4.* By an input, $U'$ satisfies the functional equation in degree $1$ over $\bar K$. $\square$

**Theorem 4.22.8 (Uniformisation from degree one).** Assume the laws and the second laws. Let $V$ be a complete discrete valuation ring of characteristic $0$, $D$ degeneration data over $V$, and $U$ a pre-uniformisation of $(A, G)$ by the pre-data of $D$ that satisfies the functional equation in degree $1$ over $\bar K$. Then there is a uniformisation of $(A, G)$ by $D$ that matches $U$.

Lean: `GlobalTheory.UU.exists_unif_of_fe_one` (also `GlobalTheory.T.exists_uniformisation_of_functionalEquation_degreeOne`, a second name).

*Proof.* *Step 1.* By an input, $U$ matches a structure $U'$ that has all data of a uniformisation except the bijectivity of the theta expansion. Fix $k \geq 1$.

*Step 2.* Since $\tau$ is bimultiplicative, an input lifts the functional equation from degree $1$ to degree $k$ over $\bar K$.

*Step 3.* By an input that uses the law on global functions, the functional equation in degree $k$ descends from $\bar K$ to $K$.

*Step 4.* By an input, every theta family of level $k$ over $K$ is the expansion of a section of $L_A^k$. With the functional equation over $K$, a second input shows that the theta expansion of $U'$ in degree $k$ is a bijection. So $U'$ is a uniformisation. $\square$

### Assembly

**Theorem 4.22.9 (Assembly).** Assume the laws and the second laws. Suppose that for every degeneration setting the conclusion of the theorem on pre-data holds, and that for every complete discrete valuation ring of characteristic $0$ the conclusion of the theorem on the functional equation in degree one holds. Let $s$ be a degeneration setting for $(A, G)$ over $V$. Then there are degeneration data $D$ over $V$ and a uniformisation $U$ of $(A, G)$ by $D$ such that $L_G = P$, the isomorphism $G_K \cong A$ is that of $s$, and the cubical structure of $L_G$ is that of $P$.

Lean: `GlobalTheory.UU.unif_assembly`.

*Proof.* The first assumption gives pre-data $D_0$ and a pre-uniformisation $U_0$ with the bundle $P$ and the isomorphism of $s$. Since $V$ is a complete discrete valuation ring, the second assumption gives degeneration data $D$ and a pre-uniformisation $U_1$ by the pre-data of $D$ with the same bundle and isomorphism, which satisfies the functional equation in degree $1$ over $\bar K$. The theorem on uniformisation from degree one gives a uniformisation $U$ by $D$ that matches $U_1$. Matching gives the three equalities. $\square$

**Theorem 4.22.10 (Degeneration data from a torsion count).** Assume the torsion count, the laws and the second laws. Let $s$ be a degeneration setting for $(A, G)$ over $V$. Then there are degeneration data $D$ over $V$ and a uniformisation $U$ of $(A, G)$ by $D$ such that $L_G = P$, the isomorphism $G_K \cong A$ is that of $s$, and the cubical structure of $L_G$ is that of $P$.

Lean: `GlobalTheory.UU.exists_degData_unif` (also `GlobalTheory.T.exists_degenerationData_uniformisation_of_torsionCount`, a second name).

*Proof.* This is the theorem on assembly applied to the theorem on pre-data and the theorem on the functional equation in degree one. $\square$

The functional equation in degree one is the only place where the choice of $\psi$ matters. The proof first builds $\psi$ from local generators, which is enough for the geometry of the thickenings, and then chooses it again from one theta section.

**Remark 4.22.11 (Formalization).** The second names are wrappers proved by a `first | exact` tactic, for example [ExistsDegenerationDataUniformisationOfTorsionCouStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/UniformizationProofs/ExistsDegenerationDataUniformisationOfTorsionCouStatement.lean#L17). The theorem on assembly takes the two earlier theorems as hypotheses instead of calling them ([UnifAssembly.lean](lean:Development/AbelianVarietyTheory/Proofs/UniformizationProofs/UnifAssembly.lean#L20)); the last theorem supplies them through their wrappers ([ExistsDegenerationDataUniformisationOfTorsionCou.lean](lean:Development/AbelianVarietyTheory/Proofs/UniformizationProofs/ExistsDegenerationDataUniformisationOfTorsionCou.lean#L22)). The torsion count is written out as a hypothesis in each statement, and the laws are the structures `Laws` and `Laws2`, proved by `GlobalTheory.T.abelianScheme_laws_unconditional`. A degeneration setting is the structure `GlobalTheory.UU.HidaSetting` ([IsCPPullback.lean](lean:Development/AbelianVarietyTheory/Definitions/Uniformization/IsCPPullback.lean#L34)); its name refers to Hida, but its fields have no relation to Hida theory. The quantification over all settings is `GlobalTheory.UU.AllSet`, and over all pre-uniformisations it is `GlobalTheory.UU.AllPre`. In the theorem on pre-data ([ExistsUniformisationDataBeforeChoice.lean](lean:Development/AbelianVarietyTheory/Proofs/UniformizationProofs/ExistsUniformisationDataBeforeChoice.lean#L280)), Steps 1 and 2 are `GlobalTheory.T.nonempty_mumfordTorusQuotientTower`, `GlobalTheory.T.nonempty_algebraisation_abelian_quotient_tower` and `GlobalTheory.T.kTriv_torusQuotientTower_algebraisation`; Steps 3 to 5 are the local lemmas `exists_weightPoints`, `DVR.exists_gen_of_local`, `exists_gtCoord_of_torusQuotient` and `exists_w` (line 241), with the uniqueness `gw_unique` at line 54. Only Step 2 uses the torsion count. In the theorem on degree one ([ExistsDegenerationDataFunctionalEquationDegreeOn.lean](lean:Development/AbelianVarietyTheory/Proofs/UniformizationProofs/ExistsDegenerationDataFunctionalEquationDegreeOn.lean#L27)), the inputs are `GlobalTheory.T.exists_integral_theta_section_with_expansion`, `GlobalTheory.T.thetaSection_support_eq_univ`, `GlobalTheory.T.exists_psi_thetaExpansionPsiRelation`, the lemma `exists_preU_setPsi`, three inputs on $\psi'$, the lemma `GlobalTheory.psiIn_maximalIdeal_of_ne_zero` and `GlobalTheory.T.thetaExpansion_functionalEquation_degree_one`. In the last of the three steps ([ExistsUniformisationOfFunctionalEquationDegreeOn.lean](lean:Development/AbelianVarietyTheory/Proofs/UniformizationProofs/ExistsUniformisationOfFunctionalEquationDegreeOn.lean#L23)), the inputs are `GlobalTheory.UU.ToChart.exists_match`, `GlobalTheory.T.functional_equation_all_degrees_algebraic_closure`, `GlobalTheory.T.finite_exponent_base_change_field`, `GlobalTheory.UU.ExpOnto.exists_expF_of_fam` and `GlobalTheory.T.expBij_of_match_of_fam_expF`. The equality of cubical structures in the conclusion is a heterogeneous equality. We did not open the proofs of the inputs, and the description of the laws lists only some of their fields. The reference to Faltings and Chai is ours.
