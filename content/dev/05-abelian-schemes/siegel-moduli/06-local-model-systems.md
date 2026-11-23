---
title: Local model systems
decls:
  - GlobalTheory.Models.exists_localSystems_ample
  - GlobalTheory.T.exists_localModelSystems_ampleFrames
  - GlobalTheory.modelsSt_of_semistableReduction
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Local model systems

The PEL moduli spaces $X_l$ of [the previous section](/entry/top-amp-exists/) live over number fields. To use them at a prime $p$, the proof of the chapter needs models over the valuation rings above $p$: for every level that is good at $p$, a normal projective flat model of $X_l$, compatible with changes of level, comparable with Siegel families, with semi-abelian schemes with split fibres, and with ample frames on a finite cover. This section states these requirements and proves that they hold, given full level models and a compatibility of moduli spaces under change of level. The background is [toroidal and minimal compactifications](/learn/abelian-varieties/#toroidal-and-minimal-compactifications) and [Néron models and good reduction](/learn/abelian-varieties/#neron-models-and-good-reduction).

Fix a CM field $E$ with a host, a PEL datum $D$ and moduli spaces $X_l$ for all levels $l$. For a coefficient field $F$ of $l$ and a valuation ring $W \subseteq \mathbb{C}$, write $V_W = W \cap F$.

**Definition 5.6.1 (Model of a moduli space).** Let $\beta : O \to F$ be a ring map. A *model* of $X_l$ over $O$ is a normal scheme $Y$, projective and flat over $O$, with a dense open immersion $j : X_{l,F} \to Y \times_O F$ over $F$, a semi-abelian scheme $G$ with $\mathcal{O}_E$-action over $Y$, and a map from the universal object, base changed to $X_{l,F}$, to $G$ over $j$, such that the abelian locus of $G_F$ is exactly the image of $j$.

Lean: `ReciprocityTheory.ChartRestriction.G.Geo.Tor.Model`, `Model.j`.

Several conditions on a model are used. It *descends* if $X_l$ is an open part of a scheme over $K_A$ with a group scheme whose base change to $F$ is $Y_F$ with $G_F$. The *level acts* if every automorphism of $X_{l,F}$ over $F$ that moves $\eta$ and $\eta_A$ by $\mathcal{O}_E$-linear maps of $\Lambda$ extends to $Y$ and $G$. A section $\sigma$ of the universal object *extends* to an open $U \subseteq Y$ if there is a section of $G$ over $U$ that restricts to $\sigma$ along $j$. A model has *good reduction extension* along a domain $V$ with fraction field $K$ if every $K$-point of $X_{l,F}$ over $V$ whose abelian variety has good reduction (an abelian scheme over $V$ with relatively ample line bundle, pulling back to the given one) extends to a $V$-point of the abelian locus of $Y$.

Lean: `Model.Descends`, `Model.LevelActs`, `Model.Extends`, `Model.GoodRedExt`.

**Definition 5.6.2 (Level structure conditions).** A model $Y$ satisfies the *level structure conditions* at $p$ if the level acts; it descends when $A = 1$; every point has a neighbourhood $V$ with sections of $L$ over $G_V$ that do not vanish simultaneously on the fibres; the sections $\eta(a)$ and $\eta_A(a)$ of order prime to $p$ extend to the abelian locus; and it has good reduction extension along every complete discrete valuation ring and along the unit ball of every algebraically closed complete field of characteristic $0$ with $|p| < 1$.

Lean: `Model.LevelStructureConditions`, `PushInvertible`.

**Definition 5.6.3 (Split fibres).** A model $Y$ has *split fibres* if at every point $y$, after a finite separable extension of the residue field, the fibre $G_y$ is a split extension of an abelian variety by a split torus.

Lean: `Model.SplitFibres`.

**Definition 5.6.4 (Ample on a cover).** A model $Y$ over $O$ is *ample on a cover* if there are an odd $m$ that is a unit in $O$, a finite surjective $\pi : Z \to Y$ and a semi-abelian scheme with $\mathcal{O}_E$-action over $Z$ mapping to $G$ over $\pi$, with [ample frames](/entry/models-nonempty-z-on-of-components/) of level $m^2$.

Lean: `GlobalTheory.LN.Amp`.

For a prime $p$ and a valuation ring $W \subseteq \mathbb{C}$ with $p$ in its maximal ideal, a *local system* at $(p, W)$ is a model $Y_{l,F}$ of $X_l$ over $V_W$ for every level $l$ good at $p$ and every coefficient field $F$ of $l$.

Lean: `ReciprocityTheory.ChartRestriction.G.Geo.Tor.LocalSystem`, `Idx`, `Coeff.V`.

**Definition 5.6.5 (Transitions and the Siegel comparison of a local system).** A local system $Y$ at $(p, W)$ satisfies *condition N2* if:

1. each $Y_{l,F}$ satisfies the level structure conditions at $p$;
2. for $l \mid l_2$ (that is, $M \mid M_2$, $\mathfrak{M}_2 \subseteq \mathfrak{M}$ and $A \mid A_2$) and $F \subseteq F_2$ there are transition maps $\pi : Y_{l_2,F_2} \to Y_{l,F}$, finite over the base change and compatible with $j$, with $\eta^{M_2/M}$ and with $\eta_A^{A_2/A}$;
3. there are a prime $n \ne p$, odd and prime to every $M$, and $j$ with $n^j \ge 3$, and a Siegel family $\mathcal{A}$ of genus $\tfrac12[E:\mathbb{Q}](p_D + q_D)$ at $p$ and level $n^j$, such that whenever $l_1$ has the same $M$ and $\mathfrak{M}$ as $l$, $A_1 = \operatorname{lcm}(A, n^j)$ and $F_1 = F(\zeta_{n^j})$, the abelian locus of $Y_{l_1, F_1}$ is finite, étale and surjective over that of $Y_{l,F}$, and maps finitely to $\mathcal{A}$ through a symplectic basis; when $p \nmid M'$ this map factors through a finite surjective map, birational on a dense open, onto a reduced flat scheme that is finite and formally unramified over $\mathcal{A}$.

Lean: `ReciprocityTheory.ChartRestriction.G.Geo.Tor.N2`, `IsTransition`, `SiegelCompare`.

**Definition 5.6.6 (Global model).** A family of local systems $Y^{p,W}$, one for each $(p, W)$, satisfies *condition N6* if for every level $l$ that is good at every prime, with $A = 1$, and every coefficient field $F$, there is a model $Y^{\mathrm{gl}}$ of $X_l$ over the ring of integers $\mathcal{O}_F$ that descends and, for every $(p, W)$, dominates the local model: there is a map from $Y^{\mathrm{gl}} \times_{\mathcal{O}_F} V_W$ to $Y^{p,W}_{l,F}$ with semi-abelian maps that is compatible with $j$ and with the maps from the universal object.

Lean: `ReciprocityTheory.ChartRestriction.G.Geo.Tor.N6`, `Dominates`.

**Definition 5.6.7 (Local model systems exist).** The statement *local model systems exist* is: for every CM field $E$ with a host, every PEL datum $D$ with $p_D + q_D \ge 1$ and all moduli spaces $X_l$, there is a family of local systems $Y^{p,W}$ such that each satisfies N2, each model in each has split fibres and is ample on a cover, and the family satisfies N6.

Lean: `GlobalTheory.LN.ModelsSt`.

The second input concerns the moduli spaces. For $l \mid l_2$ the *level compatibility* asks for a map $r : X_{l_2} \to X_l$ over $K_{A} \subseteq K_{A_2}$ compatible with $\eta^{M_2/M}$ and $\eta_A^{A_2/A}$, invariant under the automorphisms from symplectic similitudes in the congruence group of $(l, l_2)$, whose base change to a common coefficient field is finite, étale and surjective, with geometric fibres the orbits of that group and with stabilizers acting trivially at level $l_2$. The *Hecke compatibility* asks that for a prime $\mathfrak{P}$ of $\mathcal{O}_E$ with $\mathfrak{P} + \bar{\mathfrak{P}} = \mathcal{O}_E$ over a prime $p \nmid M'$, every Hecke kernel $C$ in a geometric fibre of the universal object determines exactly one point $y''$ with a surjective $\mathcal{O}_E$-linear map of points with kernel $C$, which multiplies the Weil pairing by $p^2$ and divides $\eta$ and $\eta_A$ by $p$.

Lean: `ReciprocityTheory.ChartRestriction.G.Geo.Tor.ToroidalLevelCompatibility`, `ToroidalHeckeCompatibility`.

**Definition 5.6.8 (Moduli input).** *Condition N1* is: for every CM field $E$ with a host, every PEL datum $D$ with $p_D + q_D \ge 1$ and every level $l$ a moduli space of level $l$ exists; and the level and Hecke compatibilities hold for all moduli spaces.

Lean: `ReciprocityTheory.ChartRestriction.G.Geo.Tor.N1`, `N1ab`.

We also use *the third laws*: two further facts on abelian schemes, the base change of split extensions and the pullback of the cube.

**Theorem 5.6.9 (Local model systems from full level models).** Assume the homomorphism extension theorem, the laws, the second laws, the third laws, that full level models exist, and condition N1. Then local model systems exist.

Lean: `GlobalTheory.Models.exists_localSystems_ample` (also `GlobalTheory.T.exists_localModelSystems_ampleFrames`, a second name).

*Proof.* Let $E$, $D$ with $p_D + q_D \ge 1$ and the moduli spaces $X_l$ be given. From N1 we keep the level compatibility for $D$. By [the theorem on systems of full level](/entry/exists-local-model-system-ample-frames-full-level/), proved in part two of this chapter from the same inputs and the level compatibility, there is a *system*: two auxiliary inert primes $n_0, n_1$ with exponents $J_i \ge 1$, models $T_i$ of full level $n_i^{J_i}$ with ample frames, base models over $T_i$ for every level with $A = 1$, a choice $p \mapsto n_{c(p)} \ne p$, and local systems $Y^{p,W}$ each of whose models is *raised* from a base model of the prime to $p$ part of its level, that is, lies finitely over it compatibly with $\eta$.

We take these local systems. Condition N2 holds for each of them by a lemma on transitions and Siegel clauses, and condition N6 by a lemma that glues the local models to global ones; both use the same inputs. Each model has split fibres by a lemma on local models. It remains to show that each model $Y = Y^{p,W}_{l,F}$ is ample on a cover. Let $l_0$ be the level of the base model from which $Y$ is raised, $n = n_{c(p)}$ and $T = T_{c(p)}$, with ample frames of level $(n^k)^2$. The ring $V_W$ is a Dedekind domain of characteristic $0$ with fraction field $F$, and $n$ is a unit in it since $n \ne p$ are primes; also $n$ is prime to the level $M_0$ of $l_0$. A lemma on raised models now pulls the frames of $T$ back along the finite maps $Y \to (\text{base model}) \to T$, and gives a finite surjective cover of $Y$ with ample frames of level $(n^k)^2$, with $n^k$ odd and a unit in $V_W$. $\square$

**Corollary 5.6.10 (Local model systems from semistable reduction).** The semistable reduction theorem implies that local model systems exist.

Lean: `GlobalTheory.modelsSt_of_semistableReduction`.

*Proof.* Apply the previous theorem. The homomorphism extension theorem and the three sets of laws are proved in other chapters. Full level models exist by [the corollary of the previous section](/entry/top-amp-exists-of-semistable-reduction/), from the semistable reduction theorem. Condition N1 is the theorem on moduli schemes, level maps and Hecke points; its first part is [the existence of the moduli schemes](/entry/moduli-scheme-exists/) proved in part two. $\square$

**Remark 5.6.11 (Formalization).** The proof of the theorem discards the first part of N1, the existence of moduli spaces, with `obtain ⟨-, hN⟩ := hN1`, and it also uses only the level compatibility from the second part, not the Hecke compatibility ([ExistsLocalModelSystemsAmpleFrames.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/ExistsLocalModelSystemsAmpleFrames.lean#L33)). The moduli spaces are given as data in the statement, so their existence is not needed here. The lemmas used are `T.exists_localModelSystem_ampleFrames_fullLevel`, `T.localModelSystem_transition_siegel_clauses`, `T.localModel_oneModel_and_splitFibres`, `T.raised_model_finite_cover_ample_frames` and `T.exists_global_model_of_local_models`, and the facts `CoeffRings.coeff_isDedFrac` and `Models.primeToPart_spec`; the system is the structure `GlobalTheory.Models.System`, with base models `BaseModel` and the relation `Raises`. The third laws are `Out.Laws3`, with fields `GtBaseChangeSt` and `CubePullSt`, which we did not unfold. N1 is filled in the corollary by `T.moduliScheme_levelMaps_heckePoints'`, and the homomorphism extension theorem by `homExtension_semiAbelian_dvr`. The second name is a wrapper proved by `first | exact @...` under `maxHeartbeats 1000000`.
