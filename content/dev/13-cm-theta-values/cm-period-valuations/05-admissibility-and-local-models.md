---
title: Admissibility and local models
decls:
  - GlobalTheory.TwV.admissible_at_each_site
  - GlobalTheory.TwV.site_cmpLite_siteAdm
  - GlobalTheory.T.jointSite_chain_compared_carries_admittedSystem
  - GlobalTheory.TwV.modelsOK_of_joints
  - GlobalTheory.T.thetaLocalModels_of_splitUnramified_joints
  - GlobalTheory.Svd.modelsAt_of_part
  - GlobalTheory.T.tuplesHaveLocalModels_of_standardColumnObjects
  - GlobalTheory.Svd.modelsAt_bpt
  - GlobalTheory.T.tuplesHaveLocalModels_at_constructedPoint_over_trueColumns
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Admissibility and local models

This section puts the results of Sections 1 to 4 together. At each joint site, the pending tuple of the formal group system at $p$ is admitted. From this we get *local models*: at every used tuple and every place that avoids the primes of the tuple, there are levels and a chain whose comparison maps exist and whose system is admitted. The last theorem gives local models at every constructed point whose core has a part over a column. Section 6 uses it for the first half of [the service row](/entry/serv-h-row/).

Two hypotheses run through the section. The first is the curve existence hypothesis of Section 2. The second is the *inert admissibility hypothesis*. It says that the pending tuple of a formal group system at an inert prime is admitted, once the curve condition, the hypotheses on the data below the top level, the local factorization law, the stabilizer law, and the ties at every level $j < m$ hold. Both hypotheses are theorems of a later section. The second one is [the inert theta admissibility theorem](/entry/inert-theta-admissibility-of-complex-multiplication/).

### Admitted pending tuples

A pending tuple of a formal group system is *admitted* if it satisfies the thirteen conditions of [the admissibility theorem](/entry/admissible-general-of-kernel-law/). They include Dwork's lemma at every prime, the matching of the archimedean signatures, and a Minkowski counting bound. We only use the notion through the inert admissibility hypothesis.

The *ties at level* $j$ of a pending tuple, for a ring map $\iota$, a reading $\mathrm{Rd}$ and series $\mathrm{Sr}$, are five conditions:
1. the forms at level $j$ are sharp;
2. the stabilizers act on the series by the right characters;
3. the series read the entries;
4. the series are compatible between the levels;
5. there is a constant $c_K$ with $c_K$ and $c_K^{-1}$ integral, $c_K \ne 0$, such that the kernel difference law of Section 4 holds at level $j$ with $c_K$.

Recall that a tuple $\mu$ is *used* if it is the base tuple $\mu_0$ or the tuple $\mu_w$ of a place $w$. The datum $D$ has *trivial stabilizers at step* $0$ if the stabilizers of the lattice tuples at step $0$ have the order that the orbits of places predict.

**Theorem 5.5.1 (Admitted pending tuple at a site).** Assume the inert admissibility hypothesis. Let $\mathcal{S}$ be a joint site for a joint $J$ at a used tuple $\mu$, and assume that $D$ has trivial stabilizers at step $0$. Then the pending tuple of $\mathcal{S}$ is admitted.

Lean: `GlobalTheory.TwV.admissible_at_each_site`

*Proof.* First we collect the conditions on the site from Section 3.
1. A lemma on lattice tuples gives the dictionary of the joint.
2. Given the dictionary, the pairs of lattice tuples are admissible. So the pair condition holds.
3. The place of the site induces the position embeddings.
4. Given the dictionary, the arithmetic group moves the frames. So the moves hold.
5. The away property holds, by the corollary of Section 3 on the away property from the dictionary.
6. The scalars of the series have integral powers, and with the dictionary, the pair condition and the positions this gives the condition at the unit level.

By [the three laws at a site](/entry/site-law-xi-in/) we get the kappa law, the stabilizer law and the local factorization law. The ring map $\lambda$ on $\overline{\mathbb{Q}}$ extends to an isomorphism $\iota$ of $\mathbb{C}$ with $\mathbb{C}_p$.

We apply the inert admissibility hypothesis to the system of the site, with the valuation, uniformizer and step data of the place, the bound $d_G$ on stabilizer orders below, the curve condition of the site, the unit level condition, the local factorization law and the stabilizer law. It remains to give the ties at every level $j < m$, with $\iota$, the reading of the joint through $\iota$, and the series of the pending tuple. The sharp forms come from the joint. The stabilizer tie is a lemma on the chain at the site, and it uses that $\mu$ is used and the stabilizers at step $0$ are trivial. The reading tie holds, because $\iota$ agrees with the embedding of the site on the field $L$. The compatibility of the series is a lemma on pending tuples. For the kernel difference, [the theorem on kernel differences at every level](/entry/tie-del-all-steps/) gives $c_K$ with $|c_K| = 1$. Then $|c_K| \le 1$, $|c_K^{-1}| \le 1$ and $c_K \ne 0$. $\square$

### Comparison maps and admissibility at a site

Fix a word $u$, a tuple $\mu$ and a place $w$ of residue characteristic $p$, with its index condition. Levels $L_v$ and a chain at $w$ give two conditions.

**Definition 5.5.2 (Light comparison and site admissibility).** The *light comparison* for the chain holds if there are semilinear maps $\mathrm{cmp}_j$ from the lattice space of the twist at step $j$ to the frame space of the levels at step $j$, such that $\mathrm{cmp}_0$ composed with the step map $e_0$ is the comparison map of the extra data, the maps $\mathrm{cmp}_j$ are compatible with the step maps of the chain, the twist is rational at every step $j < m$, and the valuation bound holds at step $m$. The *site admissibility* holds if $p$ is prime and there are standard data, a valuation, a uniformizer, step data, a function $d_G$ and an admitted pending tuple $Y$ for the system of the levels, with $d_G(0) = 0$ and $d_G(j) \le v_p(\Delta_\Gamma)$ for every $j$. Here $\Delta_\Gamma$ is the index constant of the member for the word $u$.

Let $\varepsilon$ be the scale of the size data and $k$ the weight of $D$. There is a constant $r_G(\varepsilon)$ that depends only on $\varepsilon$, and the weight condition is $2 r_G(\varepsilon) \le k$.

**Theorem 5.5.3 (Light comparison and admissibility from a joint).** Assume the inert admissibility hypothesis and the curve existence hypothesis. Let $t$ be a tied kernel entry and let $J$ be a joint for $t$ at $(u, \mu, w)$ with levels $L_v$, inputs $I$, hypotheses $H$ and labels $X$. Assume that $\mu$ is used, that $D$ has trivial stabilizers at step $0$, and the weight condition. Then the light comparison and the site admissibility hold for $L_v$ and the chain of $H$.

Lean: `GlobalTheory.TwV.site_cmpLite_siteAdm` (also `GlobalTheory.T.jointSite_chain_compared_carries_admittedSystem`)

*Proof.* The index condition says that $p$ is prime. The comparison inputs $I$, the hypotheses $H$ and the labels $X$ give a comparison at the chain, with maps $\mathrm{cmp}_j$, the identity at step $0$, the compatibility with the step maps, the rationality and the valuation bound. This is the light comparison.

For the site admissibility, the lattice tie of $J$ and the weight condition give standard data at $(u, w)$. By [the theorem that every joint has a site](/entry/joint-at-nonempty/), $J$ has a site $\mathcal{S}$ for these standard data. By the previous theorem the pending tuple of $\mathcal{S}$ is admitted. We take the valuation and the uniformizer of the place, and the step data. Put $d_G(0) = 0$ and $d_G(j) = v_p(\Delta_\Gamma)$ for $j \ge 1$. Then $d_G(0) = 0$, and $d_G(j) \le v_p(\Delta_\Gamma)$ in both cases. A lemma bounds the $p$-adic valuation of the order of each stabilizer at level $j$ by $d_G(j)$; this is the stabilizer bound that the previous theorem used. $\square$

### Local models

**Definition 5.5.4 (Local models).** Let $\mathrm{ex}$ be extra data over $D$, with twist $\tau$ and comparison map. The data have *local models* if:
1. $e_0(u, \mu_0) = e_{\mu_0}(u, 0)$ for every word $u$;
2. there is a choice of levels $L_v$ and a chain at every $(\mu, u, w)$ such that, whenever $\mu$ is used and $p \notin Q_p(\mu)$, the light comparison and the site admissibility hold for the chosen levels and chain.

For an object $O$ over $D$, the *local model condition* says: if the lattice tie of $O$ holds and the weight condition holds, then the extra data of $O$ have local models.

**Theorem 5.5.5 (Local models from joints).** Assume the inert admissibility hypothesis and the curve existence hypothesis. Let $t$ be a tied kernel entry for $\mathrm{ex}$ that has joints at every used tuple. Assume that $e_0(u, \mu_0) = e_{\mu_0}(u, 0)$ for every word $u$, that $D$ has trivial stabilizers at step $0$, and the weight condition. Then $\mathrm{ex}$ has local models.

Lean: `GlobalTheory.TwV.modelsOK_of_joints` (also `GlobalTheory.T.thetaLocalModels_of_splitUnramified_joints`)

*Proof.* The first condition is a hypothesis. For the second, define the choice at $(\mu, u, w)$ as follows. If $\mu$ is used and $p \notin Q_p(\mu)$, the joints at $\mu$ give levels $L_v$, inputs $I$, hypotheses $H$, labels $X$ and a joint $J$. Choose them, and take $L_v$ and the chain of $H$. Otherwise take the default levels and chain of the lattice instance. Now let $\mu$ be used and $p \notin Q_p(\mu)$. The choice is the one from the joint $J$, and the previous theorem applied to $J$ gives the light comparison and the site admissibility. $\square$

**Theorem 5.5.6 (Local models over an object with a part).** Assume the inert admissibility hypothesis and the curve existence hypothesis. Let $w$ be a column, $Z$ a later stage, and $O$ an object over $D(w, Z)$ that has a part over $(w, Z)$. Then $O$ satisfies the local model condition.

Lean: `GlobalTheory.Svd.modelsAt_of_part` (also `GlobalTheory.T.tuplesHaveLocalModels_of_standardColumnObjects`)

*Proof.* Assume the lattice tie of $O$ and the weight condition. By [the theorem on joints over an object with a part](/entry/joints-at-all-std/), there is a tied kernel entry $t$ for $\mathrm{ex}(O)$ with joints at every tuple, and $e_0(u, \mu_0) = e_{\mu_0}(u, 0)$ for every $u$. A lemma on true columns says that $D(w, Z)$ has trivial stabilizers at step $0$; its inputs are the true-column datum of $w$, its order, its laws, the stage $Z$, and the level data of $O$. The previous theorem now gives local models. $\square$

The last result is about constructed points. A *context* $\mathcal{K}$ fixes stages, a frame and twist data. A *constructed point* $\beta$ in $\mathcal{K}$ has a core $c$, a layer of objects, a part $p$ of the layer with its height, and further data. Its datum $\beta.D$ and its object $\beta.O$ come from the part. A core is *at a position with a part* if its stages come from a column $w$ and a later stage $Z$, and the core has a part over $(w, Z)$.

**Theorem 5.5.7 (Local models at a constructed point).** Assume the inert admissibility hypothesis and the curve existence hypothesis. Let $\beta$ be a constructed point whose core is at a position with a part. Then the object $\beta.O$ satisfies the local model condition over $\beta.D$.

Lean: `GlobalTheory.Svd.modelsAt_bpt` (also `GlobalTheory.T.tuplesHaveLocalModels_at_constructedPoint_over_trueColumns`)

*Proof.* We first prove: every object $O$ whose core is the core of $\beta$ satisfies the local model condition. We use the induction principle for positions. It reduces the claim to the case where the stages are the stages of a column $w$ at a later stage $Z$, and the core has a part over $(w, Z)$. In this case the part is a part of $O$, since $O$ has the same core, and the previous theorem applies.

The layer of $\beta$ gives an object at the part $p$ of $\beta$, and its core is the core of $\beta$. So this object satisfies the local model condition. The object $\beta.O$ differs from it only in the division lattice, which is the lattice of $p$ with the other prime, and in the height of $p$. A lemma on other division lattices and heights says that the local model condition passes to $\beta.O$. $\square$

**Remark 5.5.8 (Formalization).** Several facts about the Lean code:
1. The names `GlobalTheory.T.jointSite_chain_compared_carries_admittedSystem`, `GlobalTheory.T.thetaLocalModels_of_splitUnramified_joints`, `GlobalTheory.T.tuplesHaveLocalModels_of_standardColumnObjects` and `GlobalTheory.T.tuplesHaveLocalModels_at_constructedPoint_over_trueColumns` are second names, each proved by the tactic `first | exact @… | …` under `maxHeartbeats 1000000`. The file names `TuplesHaveLocalModelsAtConstructedPointOverTrueC.lean` and `…Statement.lean` are truncated.
2. `GlobalTheory.TwV.admissible_at_each_site` is a `private theorem` (JointSiteChainComparedCarriesAdmittedSystem.lean:29), so it cannot be used outside its file. It runs under `maxHeartbeats 4000000`.
3. The site admissibility `SiteAdm` (IsPlaceCofactorValuationLowerBound.lean:10) is only the conclusion `admitted` of the hypothesis `AdmAtEnt2`, together with the bound on `dG`. The light comparison `CmpLite` uses none of the hypotheses: its five parts are the fields `cmp`, `cmp_zero`, `cmp_K`, `rat` and `val` of `kaAt X H hT` (JointSiteChainComparedCarriesAdmittedSystem.lean:80).
4. The proof splits the kernel difference at $j = 0$ and $j \ge 1$ (JointSiteChainComparedCarriesAdmittedSystem.lean:63). Both branches reduce to the theorem on kernel differences at every level, so the split is not needed.
5. `AdmAtEnt2` and `LawInLt` are defined twice with the same body, in `GlobalTheory.TwV.Lt` (Definitions/GaloisGeometry/ThetaSeriesDataHypothesesBelowMaximalLevel.lean:106 and :92) and in `Formalism.L2.KerInert.AdmLoc2` (Formalism/LocalToGlobal/InertKernelTheory/ThetaSeriesDataHypothesesBelowMaximalLevel.lean:98 and :45).
6. The names say "theta", "split unramified" and "standard column objects". The statements only ask that $p \notin Q_p(\mu)$, and the hypothesis on the object is a part, not a standard tie.
7. In `GlobalTheory.Svd.modelsAt_of_part` the trivial stabilizers come from `GlobalTheory.Pdv.stepZero_trivial_stabilisers_trueColumns`, which takes the pins of the true-column datum and does not use them (StepZeroTrivialStabilisersTrueColumns.lean:91).
8. The local models are the predicate `GlobalTheory.TwU.ModelsOK` (ModelsOK.lean:56), and the local model condition is `ModelsAt` (HasPartAnd.lean:13). The choice of levels in the proof of the theorem on local models from joints uses `Classical.choose` four times (ThetaLocalModelsOfSplitUnramifiedJoints.lean:15).
