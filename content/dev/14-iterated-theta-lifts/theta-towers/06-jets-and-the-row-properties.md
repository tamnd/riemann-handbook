---
title: Periods at the top corner and the five row properties
decls:
  - GlobalTheory.T.twisted_pairing_identity
  - GlobalTheory.RowClaim.JetsAssembly.twisted_jet_one_of_all
  - GlobalTheory.RowClaim.JetsAssembly.twistedJet_succ_eq_assembly
  - GlobalTheory.T.twisted_jets_assemble
  - GlobalTheory.RowClaim.Join.thetaLift_row_properties_conj
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Periods at the top corner and the five row properties

This section evaluates the periods over the top corner of the grid, which appear in [the unfolding](/entry/twisted-theta-integral-unfolding/), as a constant times a finite class sum. This is the last of the four steps of the row formula. With the flip formula of [Theorem 3.5.6](/entry/twist-sign-flip-succ/) and the unfolding, it proves the five row properties of the twisted lifts. These properties are used in the second and third items of the step [the hypotheses are not empty](/step/nonempty-hyps/).

We keep the notation of Sections 4 and 5 and fix the local inputs of [ThetaLocalInputs](/step/theta-local-inputs-def/). All statements hold at large scale, in the sense of [the cusp step](/entry/cusp-step-of-large-flip-run/). Recall the period $\mathcal P_M(\sigma, \tau; \varphi, F)$ over the top corner for a combination $\sigma$ of pairs of polynomials on the column and the row and a combination $\tau$ of pure data.

**Definition 3.6.1 (Class sum).** Let $t$ be an index, $a$ an index of the choice and $\beta \in \mathrm{supp}_t(\Phi_a)$ a support family. For a combination $\tau$ of pure data that meets the expansion condition at $\beta$, and functions $\Psi$ on the finite points of the top node and $F'$ on the finite points of the node $(0, m)$, the class sum $S_\beta(\tau; \Psi, F')$ is a finite sum over the classes of the expansion of the values of $\Psi$ and $F'$ at the points of the class, weighted by the coefficients of $\tau$ and the class data. For $y$ a vector at $t$, let $\Psi_a$ be the finite part of the column function $\varphi_a$ and $F'_y$ the finite part of the form $F_y$.

We have not unfolded the class sum, the expansion condition or the volume condition $M$ meets at $\beta$. The point is that $S_\beta$ involves only finite points: the archimedean integrals are gone.

**Theorem 3.6.2 (Pairing identity).** Assume the sum condition. At large scale the following holds. For every pair $P$ of polynomials on the column and the row there is $\kappa \in \mathbb C$ such that for every $t$, $a$ and $\beta \in \mathrm{supp}_t(\Phi_a)$, every volume datum $M$ that meets the volume condition at $\beta$, every combination $\tau$ that meets the expansion condition at $\beta$, and every $y$,

$$\mathcal P_M(\delta_P, \tau; \varphi_a, F_y) = \kappa\, S_\beta(\tau; \Psi_a, F'_y).$$

Lean: `GlobalTheory.T.twisted_pairing_identity` (also `GlobalTheory.RowClaim.JetsAssembly.twisted_jet_one_of_all`, a second name).

*Proof.* The period is an integral over the node $(m, m)$ of the product of a lift up the column and a lift along the top row. We separate the real places from the finite places by linear functionals on the archimedean models.

First, the column function $\varphi_a$ and the form $F_y$ are given at the real places by functionals $\Lambda_0$ and $\Lambda'_0$ on the archimedean models of the top node and of $(0, m)$. These functionals can be carried up the column and along the row with the polynomials of $P$. This gives functionals $\Lambda_j$ on the models of the column nodes and $\Lambda'_i$ on those of the row nodes, such that each archimedean lift with the polynomials of $P$ is the pairing with the next functional.

Second, at the last node the two chains meet. The space at $(m, m)$ is positive definite at each real place, so the real points $K$ of its group form a compact group. Let $\kappa_0$ be its Haar probability measure. Let $s$ be the embedding of the group of $(m, m)$ into the group of the top node $X_m$ as the stabilizer of an orthogonal summand. Averaging over $K$ gives a constant $c$ with

$$\int_K \Lambda_m\bigl(\pi(s(k))^{-1} u\bigr)\, \Lambda'_m\bigl(\pi'(k)^{-1} u'\bigr)\, d\kappa_0(k) = c\, b(u, u')$$

for all vectors $u$, $u'$ of the models, where $b$ is the branching pairing between the model of $X_m$ and that of $(m, m)$. This is the compatibility of the last functionals. We take $\kappa = c$.

Third, the kernel expansion of the lifts is invariant under the levels of the volume datum at $\beta$, at the column and at the row. The sum condition, at large scale, gives the vectors of the expansion. The first row is invariant under the twist at large scale. With these facts, the period integral is glued from its pieces: the archimedean integrals are replaced by the functionals and the average at the last node, and the finite integrals become a sum over the finite points of the cells. That sum is $c$ times the class sum, by the expansion of the pairing at points: $c$ times the pairing at points of $\tau$ is the sum over the pure data $d$ of $\tau(d)$ times the pairing of the chains of $d$ against $c\, b$. $\square$

**Definition 3.6.3 (The jets condition).** The jets condition at a choice says two things. For every $t$, theta datum $\Phi$ and family $\beta$ there is a volume datum that meets the volume condition at $\beta$. For every combination $\sigma$ of pairs of polynomials there is $\kappa \in \mathbb C$ such that for every $t$, $a$, $\beta \in \mathrm{supp}_t(\Phi_a)$, $M$ and $\tau$ as in [Theorem 3.6.2](/entry/twisted-pairing-identity/), and every $y$,

$$\mathcal P_M(\sigma, \tau; \varphi_a, F_y) = \kappa\, S_\beta(\tau; \Psi_a, F'_y).$$

**Theorem 3.6.4 (Jets assembly).** Assume the sum condition. Then the jets condition holds at large scale.

Lean: `GlobalTheory.RowClaim.JetsAssembly.twistedJet_succ_eq_assembly` (also `GlobalTheory.T.twisted_jets_assemble`, a second name).

*Proof.* The period $\mathcal P_M(\sigma, \tau; \varphi, F)$ is linear in $\sigma$. So if $\kappa_P$ is the constant of [Theorem 3.6.2](/entry/twisted-pairing-identity/) for the pair $P$, then $\kappa = \sum_P \sigma(P)\, \kappa_P$ works for $\sigma$. The volume data at each $\beta$ exist because the level character of the choice meets its conditions. $\square$

We can now state the five row properties. Each holds at large scale for the choices of the row. Let $c_{\mathrm{tot}}(t)$ be the total constant of Section 5, and let $L$ be the number field of the datum with its embedding $\mathrm{emb}: L \to \mathbb C$. For a good point $x$ of the family at $t$, the choice gives the value $v(t, x, a)$ of the row sum and the value $\psi_a(\mathrm{Th}_t(j_t(x)))$ of the Fourier coefficient of the column function $a$ at the point that $x$ defines. A choice may be field-adapted. We have not unfolded these objects.

**Definition 3.6.5 (Row properties).** The five row properties are these.

1. The sum condition of Section 4.
2. The constant condition of Section 5: every square meets its nonvanishing condition and $c_{ij}(t) \neq 0$.
3. The convergence condition: for all $a$ and $u$ the convergence condition of the choice holds at $a$ and $u$.
4. The row formula: if the choice is field-adapted, there are $\kappa \in \mathbb C$ and elements $\zeta_t \in L$, each a root of unity, such that for every $t$, every good point $x$ at $t$ and every $a$,

$$\mathrm{emb}(\zeta_t)\, c_{\mathrm{tot}}(t)\, \psi_a\bigl(\mathrm{Th}_t(j_t(x))\bigr) = \kappa\, v(t, x, a).$$

5. Rationality: if the choice is field-adapted, then $v(t, x, a)$ lies in $\mathrm{emb}(L)$ for every $t$, $x$ and $a$.

The convergence condition is not unfolded here.

**Theorem 3.6.6 (Row properties of the twisted lifts).** Assume the following inputs: the local inputs; the agreement of theta integrals [ThetaIntegralsAgree](/step/theta-integrals-agree-def/) and the [local matching](/step/local-matching-def/) for the Weil tensor models; and, for the squares, the convergence of the Weil representations, a local matching and an agreement of theta integrals. Then the five row properties hold.

Lean: `GlobalTheory.RowClaim.Join.thetaLift_row_properties_conj`.

*Proof.* The constant condition follows from all six inputs by a lemma on the square constants. The condition that lifts of Fock vectors keep cusp forms follows from the local inputs. The sum condition also follows from the local inputs, and so does the convergence condition, with the condition on Fock vectors.

The row formula follows from four steps, the constant condition and the sum condition, by a lemma on the principal level. The four steps are these.

1. The projection step: the lift at a good point is fixed by the idempotent $e_0$ of the real datum. It follows from a period identity for the local inputs.
2. The flip step, by [Theorem 3.5.6](/entry/twist-sign-flip-succ/), with the convergence on the squares, the agreement of theta integrals for the Weil tensor models and the constant condition.
3. The unfolding step, by [Theorem 3.4.7](/entry/twisted-theta-integral-unfolding/), with the sum condition.
4. The jets step, by [Theorem 3.6.4](/entry/twisted-jet-succ-eq-assembly/), with the sum condition.

Together the steps express the twisted theta function at the lift of $y$ through the opposite path, the periods at the top corner and the class sums, with the constants $(z_t c_{\mathrm{tot}}(t))^{-1}$, $z_t^{-1} s$ and $\kappa$. The lemma on the principal level turns this into the row formula; we have not opened its proof.

Rationality follows from the sum condition, by a lemma on finite sums. $\square$

**Remark 3.6.7 (Formalization).** The lemmas that give the constant condition, the condition on Fock vectors, the sum condition, the convergence condition, the projection step, the lemma on the principal level and the rationality are not in this chapter, and we have not opened them; the proof above names them by what they give. The convergence condition is given by a lemma whose name speaks of linear independence of twisted characters ([ThetaLiftRowPropertiesConj.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/ThetaLiftRowPropertiesConj.lean#L21)). The local matching for the Weil tensor models, and the local matching and theta integrals for the squares, are used only for the constant condition. The jets theorem is named for a successor step, but it has none. The pairing identity has a second name at line 16 of [TwistedJetSuccEqAssembly.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedJetSuccEqAssembly.lean#L16), a term equal to it. The row properties theorem has a renaming with the same statement at line 30 of its file.
