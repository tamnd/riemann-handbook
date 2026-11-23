---
title: The twisted torsion class theorem
decls:
  - GlobalTheory.T.theorem_tb_of_local_blochKato_duality_euler
  - GlobalTheory.TheoremTBRecords.aux_of_blochKato_tateDuality_eulerChar
  - GlobalTheory.T.twistedTorsionClassTheorem_goodCase
  - GlobalTheory.TheoremTB.tb_assembled
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The twisted torsion class theorem

The twisted torsion class theorem joins two local statements about the rank one twists $L(\chi^{-e})$ at every prime $\ell$ and every good triple. The first is the bound of [Theorem 6.6.7](/entry/crystalline-extension-class-bound/) on the class of a crystalline extension. The second bounds the torsion of $H^1$ modulo $H^1_f$ and computes $H^1_f$ for these twists. This section proves the theorem from three published inputs: the local results of Bloch and Kato, local Tate duality and the local Euler characteristic formula. It is the local input at the row places of [Theorem 6.2.2](/entry/selmer-bound-at-point-main/), and so an input of the step [EveryCharacter from theta integrals and local matching](/step/theta-local-matching/). We use the [Bloch-Kato groups](/learn/padic-hodge/#local-bloch-kato-theory) and the [[Galois cohomology|9MPCZ3EAJM]] of local fields of [the Background](/learn/galois-cohomology/#local-fields).

We keep the notation of the previous section: $\ell$, a good triple $(K, s, L)$ with its Wach and comparison data, the cyclotomic character $\chi$, the number $g_K$, the exponent $c(N_Y)$ and the module $H^1_f(K, V/T_V)$. For a lattice representation $V$ let $H^1(K, V/T_V)$ be the module of cocycles $G_K \to V/T_V$ modulo coboundaries, and let $I_K \subseteq G_K$ be the inertia subgroup.

**Definition 6.7.1 (Twisted torsion statements).** Fix a good triple $(K, s, L)$. The statement $\mathrm{TB}(K, s, L)$ is the conclusion of [Theorem 6.6.7](/entry/crystalline-extension-class-bound/) for all $e$, $M_0$, $h_0$, $Y$, $\tilde Y$, $Z$, $V_e$, $\iota$, $\pi$, $\tilde y$, $\phi$ and $f$ that satisfy its hypotheses. The statement $\mathrm{TB}_e(K, s, L)$ says: for every $e \in \mathbb{N}$ and every lattice representation $V_e$ with $\dim V_e = 1$ on which $g$ acts by $\chi(g)^{-e}$,

1. for every $n$, the $\ell^n$-torsion of $H^1(K, V_e/T_e)/H^1_f(K, V_e/T_e)$ has $\mathcal{O}$-length at most $([K : \mathbb{Q}_\ell] + 1)\, n \cdot \mathrm{length}_{\mathcal{O}}(\mathcal{O}/\ell)$;
2. if $e > 0$, every Bloch-Kato cocycle of $V_e/T_e$ is a coboundary;
3. if $e = 0$, a map $c : G_K \to V_e/T_e$ is a Bloch-Kato cocycle exactly when $c$ is a cocycle and there is $x$ with $c(g) = g x - x$ for all $g \in I_K$.

The *twisted torsion statements* hold if $\mathrm{TB}(K, s, L)$ and $\mathrm{TB}_e(K, s, L)$ hold for every prime $\ell$ and every good triple.

Lean: `Formalism.MainNotions.LocalSituation.Conclusion4` (also `Formalism.MainNotions.LocalSituation.TBat` and `Formalism.MainNotions.LocalSituation.TBeAt`, the two statements at one triple).

In clause 3, for $e = 0$, the Bloch-Kato cocycles are the unramified ones. In clause 2, for $e > 0$, the group $H^1_f$ is zero. Clause 1 bounds how far $H^1$ is from $H^1_f$.

**Definition 6.7.2 (Local Bloch-Kato package).** The *local Bloch-Kato package* holds if, for every prime $\ell$ and every finite extension $K$ of $\mathbb{Q}_\ell$, the following five statements hold for representations over finite extensions $L$ of $\mathbb{Q}_\ell$:

1. for a de Rham representation $V$ and its dual $V'$, under the cup product into $L(1)$, the groups $H^1_f(K, V)$ and $H^1_f(K, V')$ are the exact annihilators of each other;
2. for a de Rham $V$, $\dim H^1_f(K, V) = \dim H^0(K, V) + \dim D_{\mathrm{dR}}(V) - \dim \mathrm{Fil}^0 D_{\mathrm{dR}}(V)$;
3. a surjection $V \to V'$ of crystalline representations is surjective on $H^1_f$ at the level of cocycles, up to coboundaries;
4. the integral form of 1: for dual lattices in de Rham representations, a cocycle with values in $V'/T'$ is a Bloch-Kato cocycle exactly when its cup product with every Bloch-Kato cocycle of $T$ is a coboundary in the cyclotomic lattice, and the same with the roles exchanged;
5. the form of 4 with coefficients $T/\varpi^r T$.

Lean: `Formalism.MainNotions.LocalSituation.Conclusion5` (also `Formalism.MainNotions.LocalSituation.bkAll`).

**Theorem 6.7.3 (Twisted torsion statements from the local facts).** Assume the admitted local facts and the local Bloch-Kato package. Then the twisted torsion statements hold.

Lean: `GlobalTheory.TheoremTB.tb_assembled` (also `GlobalTheory.T.twistedTorsionClassTheorem_goodCase`, a second name).

*Proof.* Fix $\ell$ and a good triple $(K, s, L)$. The statement $\mathrm{TB}(K, s, L)$ is [Theorem 6.6.7](/entry/crystalline-extension-class-bound/), which uses only the admitted local facts. The statement $\mathrm{TB}_e(K, s, L)$ is a theorem proved elsewhere in this development from the admitted local facts and the local Bloch-Kato package. $\square$

The three published inputs are stated next. Local Tate duality and the local Euler characteristic formula are those of [Theorem 6.1.5](/entry/local-duality-class-field-facts-of-artin-tate-euler/).

**Definition 6.7.4 (Local results of Bloch and Kato).** The *local results of Bloch and Kato* hold if, for every prime $\ell$, every set of local period data at $\ell$ that is tied to its $A_{\inf}$ data, and every finite extension $K$ of $\mathbb{Q}_\ell$, the following three statements hold for representations over $\mathbb{Q}_\ell$:

1. the dimension formula 2 of the local Bloch-Kato package, with $H^1_f(K, V)$ finite-dimensional;
2. the rational duality 1 of the package;
3. the integral duality 4 of the package, with $\mathbb{Z}_\ell$-lattices.

Lean: `GlobalTheory.Published.BlochKatoLocal`.

These are the results of Bloch and Kato in the cited work, §3.

**Theorem 6.7.5 (Twisted torsion class theorem).** Assume the local results of Bloch and Kato, local Tate duality and the local Euler characteristic formula. Then for every datum and all Wach, comparison and Fontaine data over it, the twisted torsion statements hold.

Lean: `GlobalTheory.TheoremTBRecords.aux_of_blochKato_tateDuality_eulerChar` (also `GlobalTheory.T.theorem_tb_of_local_blochKato_duality_euler`, a second name).

*Proof.* Two results proved elsewhere in this development reduce the hypotheses of the previous Theorem to the three inputs. First, the nine admitted local facts hold. Facts 2 and 4 are local Tate duality and the local Euler characteristic formula. Fact 3 follows from local Tate duality, and the remaining six facts are proved without further inputs. Second, the local Bloch-Kato package follows from the three inputs. The previous Theorem then gives the twisted torsion statements. $\square$

**Remark 6.7.6 (Formalization).** In [TheoremTbOfLocalBlochKatoDualityEuler.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TheoremTbOfLocalBlochKatoDualityEuler.lean#L16), the comparison datum `Cm` is introduced as `_Cm` and never used, since `Conclusion4` does not mention it. The proof obtains `⟨_J, hA⟩` from `GlobalTheory.LocInputs.ties_and_inputs_of_duality_euler` and discards the ties `_J` (line 17). The local Bloch-Kato package is `GlobalTheory.T.blochKatoLocal_all_of_tateDuality_eulerChar`. In [TiesAndInputsOfDualityEuler.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TiesAndInputsOfDualityEuler.lean#L19), the admitted facts come from `surjective_half_of_onto`, the two inputs, `tate_h2_of_local_duality`, `tate_fil_quot`, `fundamentalExactSequence_continuity_all_theories`, `fontaine_bounds`, `TateDualFil.main`, `FontW.main` and `decompletion`. So the hypothesis `admitted` of [CrystallineExtensionClassBound.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CrystallineExtensionClassBound.lean#L359) is a theorem once the two inputs are given. The statement $\mathrm{TB}_e$ is `GlobalTheory.T.weight_good_reduction_at_prime`, whose proof we did not open. We did not unfold `divisibleCocycles`, `IK`, `LocTied` or the cup products. In [TwistedTorsionClassTheoremGoodCase.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TwistedTorsionClassTheoremGoodCase.lean#L12), the local Bloch-Kato package goes only into $\mathrm{TB}_e$. Both second names are proved by `first | exact ...` under `maxHeartbeats 1000000`, which a one-line proof does not need.
